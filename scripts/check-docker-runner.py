from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from harness.judge_core import DockerRunner


def require_docker() -> None:
    if shutil.which("docker") is None:
        raise SystemExit("docker CLI is not installed")
    probe = subprocess.run(["docker", "info"], capture_output=True, text=True)
    if probe.returncode != 0:
        raise SystemExit(f"docker daemon is not available:\n{probe.stderr.strip()}")


def assert_run(label: str, lang: str, code: str, stdin: str, expected: str) -> None:
    result = DockerRunner().run(
        lang,
        code,
        stdin,
        time_limit_s=2.0,
        memory_mb=512,
        max_output_bytes=1024 * 1024,
    )
    if not result.ok or result.stdout.strip() != expected:
        raise SystemExit(
            f"{label} failed: ok={result.ok} exit={result.exit_code} "
            f"stdout={result.stdout!r} stderr={result.stderr!r}"
        )


def main() -> int:
    require_docker()
    assert_run("python", "python", "print(input()[::-1])\n", "abc\n", "cba")
    assert_run(
        "cpp",
        "cpp",
        '#include <bits/stdc++.h>\nusing namespace std;\nint main(){int a,b;cin>>a>>b;cout<<a+b<<"\\n";}\n',
        "2 3\n",
        "5",
    )
    assert_run(
        "java",
        "java",
        "import java.io.*;import java.util.*;public class Main{public static void main(String[]a)throws Exception{Scanner s=new Scanner(System.in);System.out.println(s.nextInt()*s.nextInt());}}\n",
        "6 7\n",
        "42",
    )
    print("Docker runner check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
