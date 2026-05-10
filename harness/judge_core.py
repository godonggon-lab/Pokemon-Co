"""
하네스 채점 코어.

흐름:
  1) 입력 케이스 N개 생성 (harness.generators)
  2) Oracle 코드를 각 입력으로 실행 → 기대 출력 수집
  3) 사용자 코드를 각 입력으로 실행 → 실제 출력 비교
  4) 결과 verdict 반환 (AC/WA/RE/TLE/CE/ERR)

Runner 인터페이스:
  run(lang, code, stdin, *, time_limit_s, memory_mb) -> RunResult

기본 Runner 두 개 제공:
  - LocalRunner   : subprocess (개발 편의용, 격리 없음 — 신뢰된 oracle 전용/CI 용)
  - DockerRunner  : `docker run --network=none --read-only ...` (사용자 코드용, 권장)

서버는 사용자 코드 = DockerRunner / oracle = LocalRunner 로 분리해 호출한다.
"""
from __future__ import annotations
import json
import os
import shutil
import subprocess
import tempfile
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Protocol

Lang = Literal["python", "cpp", "javascript", "java"]


@dataclass
class RunResult:
    ok: bool
    stdout: str
    stderr: str
    duration_ms: int
    timed_out: bool
    compile_error: bool
    oom_killed: bool = False
    output_exceeded: bool = False
    exit_code: int = 0


class Runner(Protocol):
    def run(
        self,
        lang: Lang,
        code: str,
        stdin: str,
        *,
        time_limit_s: float,
        memory_mb: int,
        max_output_bytes: int = 64 * 1024 * 1024,
    ) -> RunResult: ...


def _normalize(s: str) -> str:
    """라인 끝 공백과 마지막 개행에 관대한 비교용 정규화."""
    return "\n".join(line.rstrip() for line in s.replace("\r\n", "\n").rstrip().split("\n"))


def _normalize_tokens(s: str) -> str:
    """토큰 단위 비교용 정규화. PE 판정에만 사용한다."""
    return " ".join(s.split())


def _decode_limited(data: bytes, limit: int) -> tuple[str, bool]:
    exceeded = len(data) > limit
    if exceeded:
        data = data[:limit]
    return data.decode("utf-8", "replace"), exceeded


# --------------------------- LocalRunner (oracle 전용 권장) ---------------------------
class LocalRunner:
    def run(self, lang, code, stdin, *, time_limit_s=2.0, memory_mb=256, max_output_bytes=64 * 1024 * 1024):
        with tempfile.TemporaryDirectory() as tmp:
            try:
                cmd = self._compile(lang, code, tmp)
            except subprocess.CalledProcessError as ce:
                return RunResult(False, "", ce.stderr.decode("utf-8", "replace") if ce.stderr else str(ce),
                                 0, False, True)
            except FileNotFoundError as fe:
                return RunResult(False, "", f"compiler/runtime not found: {fe.filename}", 0, False, True)
            t0 = time.perf_counter()
            try:
                p = subprocess.run(cmd, input=stdin.encode("utf-8"),
                                   capture_output=True, timeout=time_limit_s, cwd=tmp)
            except subprocess.TimeoutExpired:
                return RunResult(False, "", "", int((time.perf_counter() - t0) * 1000), True, False)
            dur = int((time.perf_counter() - t0) * 1000)
            stdout, output_exceeded = _decode_limited(p.stdout, max_output_bytes)
            return RunResult(
                ok=(p.returncode == 0 and not output_exceeded),
                stdout=stdout,
                stderr=p.stderr.decode("utf-8", "replace"),
                duration_ms=dur, timed_out=False, compile_error=False,
                output_exceeded=output_exceeded,
                exit_code=p.returncode
            )

    def _compile(self, lang, code, tmp):
        if lang == "python":
            f = os.path.join(tmp, "main.py")
            with open(f, "w", encoding="utf-8") as h: h.write(code)
            return ["python", f]
        if lang == "javascript":
            f = os.path.join(tmp, "main.js")
            with open(f, "w", encoding="utf-8") as h: h.write(code)
            return ["node", f]
        if lang == "cpp":
            src = os.path.join(tmp, "main.cpp"); exe = os.path.join(tmp, "a.out")
            with open(src, "w", encoding="utf-8") as h: h.write(code)
            subprocess.run(["g++", "-O2", "-std=gnu++17", src, "-o", exe], check=True, capture_output=True)
            return [exe]
        if lang == "java":
            src = os.path.join(tmp, "Main.java")
            with open(src, "w", encoding="utf-8") as h: h.write(code)
            subprocess.run(["javac", "-encoding", "UTF-8", src], check=True, capture_output=True, cwd=tmp)
            return ["java", "-cp", tmp, "Main"]
        raise ValueError(f"unknown lang {lang}")


# --------------------------- DockerRunner (사용자 코드용) ---------------------------
class DockerRunner:
    """`code-runner` 이미지를 사전 빌드한 뒤 사용. (judge/Dockerfile 참조)
    --network=none, --read-only, --memory, --cpus, ulimit 로 자원 제한.
    """
    IMAGE = os.environ.get("CODERUNNER_IMAGE", "dongjun-coderunner:latest")

    def run(self, lang, code, stdin, *, time_limit_s=2.0, memory_mb=256, max_output_bytes=64 * 1024 * 1024):
        if shutil.which("docker") is None:
            return RunResult(False, "", "docker not installed on judge host", 0, False, False)

        tmp_root = Path(os.environ.get("CODERUNNER_TMPDIR", Path.cwd() / ".data" / "runner-tmp"))
        tmp_root.mkdir(parents=True, exist_ok=True)
        host_dir = tempfile.mkdtemp(prefix="cr-", dir=str(tmp_root))
        fname = {"python":"main.py","javascript":"main.js","cpp":"main.cpp","java":"Main.java"}[lang]
        os.chmod(host_dir, 0o755)
        source_path = os.path.join(host_dir, fname)
        with open(source_path, "w", encoding="utf-8") as h: h.write(code)
        os.chmod(source_path, 0o644)
        host_mount = str(Path(host_dir).resolve()).replace("\\", "/")

        cname = f"cr-{uuid.uuid4().hex[:10]}"
        # 컨테이너 내부 timeout 을 정확한 ms 로 강제. 외부 subprocess 타임아웃은
        # 컨테이너가 어떤 이유로든 멈췄을 때를 대비한 안전망 (작게 잡는다).
        time_limit_ms = int(round(time_limit_s * 1000))
        outer_timeout_s = time_limit_s + 2  # 컨테이너 startup overhead 여유
        cmd = [
            "docker", "run", "--rm", "-i",
            "--name", cname,
            "--network", "none",
            "--read-only",
            "--cap-drop", "ALL",
            "--security-opt", "no-new-privileges",
            "--tmpfs", "/work:exec,size=64m,mode=1777",
            "--memory", f"{memory_mb}m",
            "--memory-swap", f"{memory_mb}m",
            "--cpus", "1.0",
            "--pids-limit", "128",
            "--ulimit", "nofile=64:64",
            "-v", f"{host_mount}:/code:ro",
            "-e", f"LANG_NAME={lang}",
            "-e", f"TIME_LIMIT_MS={time_limit_ms}",
            self.IMAGE
        ]
        t0 = time.perf_counter()
        try:
            p = subprocess.run(cmd, input=stdin.encode("utf-8"),
                               capture_output=True, timeout=outer_timeout_s + 5)
        except subprocess.TimeoutExpired:
            subprocess.run(["docker", "kill", cname], capture_output=True)
            return RunResult(False, "", "", int((time.perf_counter() - t0) * 1000), True, False)
        finally:
            shutil.rmtree(host_dir, ignore_errors=True)

        dur = int((time.perf_counter() - t0) * 1000)
        out, output_exceeded = _decode_limited(p.stdout, max_output_bytes)
        err = p.stderr.decode("utf-8", "replace")
        # 컨테이너 내부 entrypoint 가 컴파일 실패 시 종료코드 100 약속
        compile_error = (p.returncode == 100)
        # TLE 감지: 컨테이너 내부 `timeout` 명령어가 종료코드 124 (SIGTERM 시) 또는
        # 128+15=143 (SIGTERM exit) 또는 --kill-after 후 137 일 수 있다.
        # 단, 137 은 OOM(cgroup kill) 과도 겹치므로 stderr/duration 으로 분간한다.
        timed_out = (p.returncode == 124) or (p.returncode == 143)
        # OOM 감지: 종료코드 137 + 메모리 관련 stderr 또는 메모리 한계 근접
        oom_killed = (
            ("MemoryError" in err) or ("std::bad_alloc" in err) or ("OutOfMemoryError" in err)
            or (p.returncode == 137 and dur < (time_limit_ms + 500))
        )
        # 137 인데 OOM 신호도 없고 시간이 한계 근처면 TLE 의 강제 kill 로 간주
        if p.returncode == 137 and not oom_killed and dur >= time_limit_ms:
            timed_out = True
        return RunResult(
            ok=(p.returncode == 0 and not output_exceeded),
            stdout=out, stderr=err,
            duration_ms=dur, timed_out=timed_out, compile_error=compile_error,
            oom_killed=oom_killed, output_exceeded=output_exceeded, exit_code=p.returncode
        )


# --------------------------- 채점 본체 ---------------------------
@dataclass
class CaseResult:
    idx: int
    input: str
    expected: str
    actual: str
    ok: bool
    kind: str  # sample | edge | stress | fuzz
    verdict: str = "AC"  # AC | WA | PE | TLE | MLE | OLE | RE
    duration_ms: int = 0


@dataclass
class JudgeCase:
    input: str
    kind: str  # sample | edge | stress | fuzz
    expected: str | None = None


def _coerce_generated_case(item: object) -> JudgeCase:
    if isinstance(item, str):
        return JudgeCase(input=item, kind="fuzz")
    if isinstance(item, dict):
        stdin = item.get("input")
        if not isinstance(stdin, str):
            raise ValueError("generated case dict must contain string input")
        kind = item.get("kind", "fuzz")
        if kind not in {"edge", "stress", "fuzz"}:
            raise ValueError(f"unsupported generated case kind: {kind}")
        expected = item.get("expected")
        if expected is not None and not isinstance(expected, str):
            raise ValueError("generated case expected must be string when provided")
        return JudgeCase(input=stdin, kind=kind, expected=expected)
    raise ValueError(f"unsupported generated case type: {type(item).__name__}")


def _compare_output(actual: str, expected: str) -> tuple[bool, str]:
    if _normalize(actual) == _normalize(expected):
        return True, "AC"
    if _normalize_tokens(actual) == _normalize_tokens(expected):
        return False, "PE"
    return False, "WA"


def _problem_id_from_slug(problem_slug: str) -> str | None:
    tail = problem_slug.rsplit("-", 1)[-1]
    return tail if tail.isdigit() else None


def _load_sample_cases(problem_slug: str, *, max_samples: int = 3) -> list[JudgeCase]:
    problem_id = _problem_id_from_slug(problem_slug)
    if not problem_id:
        return []

    path = Path(__file__).resolve().parent.parent / "data" / "problems-statements.json"
    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []

    statement = data.get(problem_id)
    if not isinstance(statement, dict) or statement.get("_failed"):
        return []

    cases: list[JudgeCase] = []
    for sample in statement.get("samples") or []:
        if not isinstance(sample, dict):
            continue
        stdin = sample.get("in")
        expected = sample.get("out")
        if isinstance(stdin, str) and isinstance(expected, str):
            cases.append(JudgeCase(input=stdin, kind="sample", expected=expected))
        if len(cases) >= max_samples:
            break
    return cases


def judge(*,
          problem_slug: str,
          category_slug: str,
          user_lang: Lang,
          user_code: str,
          oracle_lang: Lang,
          oracle_code: str,
          user_runner: Runner,
          oracle_runner: Runner,
          case_count: int = 6,
          time_limit_s: float = 2.0,
          memory_limit_mb: int = 256,
          max_output_bytes: int = 64 * 1024 * 1024) -> dict:
    from .generators import generate, replaces_samples
    try:
        sample_cases = [] if replaces_samples(problem_slug) else _load_sample_cases(problem_slug)
        fuzz_cases = [
            _coerce_generated_case(case)
            for case in generate(problem_slug, category_slug, count=case_count)
        ]
    except Exception as e:
        return {
            "status": "ERR",
            "message": f"generator failed: {e}",
            "durationMs": 0
        }
    judge_cases = sample_cases + fuzz_cases
    if not judge_cases:
        return {
            "status": "ERR",
            "message": "no valid judge cases available: add BOJ samples or a problem-specific fuzz override",
            "durationMs": 0
        }

    cases: list[CaseResult] = []
    passed = 0
    t0 = time.perf_counter()

    for i, jc in enumerate(judge_cases):
        stdin = jc.input
        expected = jc.expected
        if expected is None:
            # 1) Oracle 실행
            oracle = oracle_runner.run(oracle_lang, oracle_code, stdin,
                                       time_limit_s=time_limit_s * 2, memory_mb=512,
                                       max_output_bytes=max_output_bytes)
            if not oracle.ok:
                if oracle.compile_error:
                    reason = "compile error"
                elif oracle.output_exceeded:
                    reason = "output limit"
                elif oracle.timed_out:
                    reason = "time limit"
                elif oracle.oom_killed:
                    reason = "memory limit"
                else:
                    reason = f"exit code {oracle.exit_code}"
                return {
                    "status": "ERR",
                    "message": f"oracle failed on {jc.kind} case #{i}: {reason}\n{oracle.stderr}".strip(),
                    "cases": [c.__dict__ for c in cases],
                    "durationMs": int((time.perf_counter() - t0) * 1000)
                }
            expected = oracle.stdout

        # 2) 사용자 실행
        user = user_runner.run(user_lang, user_code, stdin,
                               time_limit_s=time_limit_s, memory_mb=memory_limit_mb,
                               max_output_bytes=max_output_bytes)
        if user.compile_error:
            return {"status": "CE", "message": user.stderr,
                    "durationMs": int((time.perf_counter() - t0) * 1000)}
        if user.output_exceeded:
            cases.append(CaseResult(i, stdin, expected, "<OLE>", False, jc.kind,
                                    verdict="OLE", duration_ms=user.duration_ms))
            continue
        if user.timed_out:
            cases.append(CaseResult(i, stdin, expected, "<TLE>", False, jc.kind,
                                    verdict="TLE", duration_ms=user.duration_ms))
            continue
        if user.oom_killed:
            cases.append(CaseResult(i, stdin, expected, "<MLE>", False, jc.kind,
                                    verdict="MLE", duration_ms=user.duration_ms))
            continue
        if not user.ok:
            cases.append(CaseResult(i, stdin, expected, user.stderr or "<RE>", False, jc.kind,
                                    verdict="RE", duration_ms=user.duration_ms))
            continue
        ok, verdict = _compare_output(user.stdout, expected)
        if ok: passed += 1
        cases.append(CaseResult(i, stdin, expected, user.stdout, ok, jc.kind,
                                verdict=verdict, duration_ms=user.duration_ms))

    total = len(cases)
    # 우선순위: CE > MLE > TLE > OLE > RE > PE > WA > AC
    verdicts = [c.verdict for c in cases]
    if total == 0:
        status = "WA"
    elif passed == total:
        status = "AC"
    elif "MLE" in verdicts:
        status = "MLE"
    elif "TLE" in verdicts:
        status = "TLE"
    elif "OLE" in verdicts:
        status = "OLE"
    elif "RE" in verdicts:
        status = "RE"
    elif "PE" in verdicts:
        status = "PE"
    else:
        status = "WA"
    return {
        "status": status,
        "passed": passed,
        "total": total,
        "cases": [c.__dict__ for c in cases],
        "durationMs": int((time.perf_counter() - t0) * 1000)
    }
