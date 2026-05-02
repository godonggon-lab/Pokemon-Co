"use client";

import dynamic from "next/dynamic";
import { useEffect, useMemo, useRef, useState } from "react";
import type { Problem, Source, Category } from "@/lib/types";
import { useTrainer } from "./TrainerProvider";
import { applyOutcome } from "@/lib/rating";
import CaptureAnimation, { type CaptureEvent } from "./CaptureAnimation";
import { buildMonster, getMonsterEntry } from "@/lib/characters";
import { buildFlavor } from "@/lib/flavor";
import { getProblemMeta } from "@/lib/meta";

// category 는 현재 사용처가 빌드 정보 정도지만 미래확장 위해 유지

const Editor = dynamic(() => import("@monaco-editor/react"), { ssr: false });

type CaseResult = {
  idx: number; input: string; expected: string; actual: string;
  ok: boolean; kind: "sample" | "fuzz";
  verdict?: "AC" | "WA" | "TLE" | "MLE" | "RE";
  duration_ms?: number;
};
type JudgeStatus = "AC" | "WA" | "TLE" | "MLE" | "RE" | "CE" | "ERR";
type JudgeVerdict =
  | { status: "AC" | "WA" | "TLE" | "MLE" | "RE"; passed: number; total: number; cases: CaseResult[]; durationMs: number }
  | { status: "CE" | "ERR"; message: string; cases?: CaseResult[]; durationMs?: number };
type RunStatus = "OK" | "TLE" | "MLE" | "RE" | "CE" | "ERR";
type RunVerdict = {
  status: RunStatus;
  stdout?: string;
  stderr?: string;
  message?: string;
  durationMs?: number;
  exitCode?: number;
};

const STARTER: Record<string, string> = {
  python:     "import sys\ninput = sys.stdin.readline\n\n# 여기에 풀이를 작성하세요\n",
  cpp:        "#include <bits/stdc++.h>\nusing namespace std;\nint main(){\n    // 여기에 풀이를 작성하세요\n    return 0;\n}\n",
  javascript: "// 여기에 풀이를 작성하세요 (process.stdin 사용)\n",
  java:       "import java.util.*;\npublic class Main {\n  public static void main(String[] args){\n    // 여기에 풀이를 작성하세요\n  }\n}\n"
};

// 사용자 제출 가능한 언어는 모든 문제에서 python/cpp/java 로 통일.
// (oracle 코드가 다른 언어라도, 채점은 oracle 출력과의 일치 여부로만 판단되므로
//  문제별 sources 의 언어 구성과 무관하게 항상 세 언어로 풀 수 있다.)
const SUBMIT_LANGS: Source["lang"][] = ["python", "cpp", "java"];

export default function ProblemPlayground({
  problem, category
}: { problem: Problem; category: Category }) {
  const langs = SUBMIT_LANGS;
  const [lang, setLang] = useState<Source["lang"]>("python");
  const [code, setCode] = useState<string>(STARTER["python"] ?? "");
  const [submitting, setSubmitting] = useState(false);
  const [running, setRunning] = useState(false);
  const [verdict, setVerdict] = useState<JudgeVerdict | null>(null);
  const [runVerdict, setRunVerdict] = useState<RunVerdict | null>(null);
  const [showOracle, setShowOracle] = useState(false);
  const [capture, setCapture] = useState<CaptureEvent | null>(null);
  const [customInput, setCustomInput] = useState("");
  const [draftStatus, setDraftStatus] = useState<"loaded" | "saved" | "">("");
  const submitRef = useRef<() => void>(() => {});

  const { profile, ready, applyWin, applyLoss, bumpAttempt } = useTrainer();
  const draftKey = useMemo(() => `codedex:draft:${problem.slug}:${lang}`, [problem.slug, lang]);
  const inputKey = useMemo(() => `codedex:stdin:${problem.slug}`, [problem.slug]);
  const flavorLimits = useMemo(() => {
    const monsterEntry = getMonsterEntry(problem.slug);
    return monsterEntry
      ? buildFlavor(problem, monsterEntry, getProblemMeta(problem.id)).limits
      : undefined;
  }, [problem]);

  useEffect(() => {
    const saved = window.localStorage.getItem(draftKey);
    setCode(saved ?? STARTER[lang] ?? "");
    setDraftStatus(saved ? "loaded" : "");
  }, [draftKey, lang]);

  useEffect(() => {
    const savedInput = window.localStorage.getItem(inputKey);
    setCustomInput(savedInput ?? "");
  }, [inputKey]);

  useEffect(() => {
    window.localStorage.setItem(draftKey, code);
    setDraftStatus("saved");
  }, [code, draftKey]);

  useEffect(() => {
    window.localStorage.setItem(inputKey, customInput);
  }, [customInput, inputKey]);

  function onLangChange(next: Source["lang"]) {
    setLang(next);
    setVerdict(null);
    setRunVerdict(null);
  }

  async function submit() {
    if (!ready || !profile) return;
    setSubmitting(true); setVerdict(null);

    bumpAttempt(problem.slug);
    const attemptsBefore = (profile.attempts[problem.slug] ?? 0) + 1;

    try {
      const r = await fetch("/api/judge", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          problemSlug: problem.slug, lang, code,
          limits: flavorLimits
        })
      });
      const j: JudgeVerdict = await r.json();
      setVerdict(j);

      const win = j.status === "AC";
      const delta = applyOutcome({
        prevTR: profile.tr,
        problemId: problem.id,
        categorySlug: problem.categorySlug,
        attempts: attemptsBefore,
        win
      });

      if (win) {
        const m = buildMonster(problem);
        const res = await applyWin(problem.slug, delta);
        setCapture({
          monsterName: m.name,
          spriteUrl: m.artworkUrl,
          fallbackEmoji: m.fallbackEmoji,
          delta: delta.delta,
          newTR: delta.nextTR,
          firstCapture: res.firstCapture
        });
      } else if (j.status === "WA" || j.status === "TLE" || j.status === "MLE" || j.status === "RE") {
        applyLoss(problem.slug, delta);
      }
    } catch (e: any) {
      setVerdict({ status: "ERR", message: e?.message ?? "network error" });
    } finally {
      setSubmitting(false);
    }
  }

  submitRef.current = submit;

  async function runCustomInput() {
    setRunning(true);
    setRunVerdict(null);
    try {
      const r = await fetch("/api/judge", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          mode: "run",
          problemSlug: problem.slug,
          lang,
          code,
          stdin: customInput,
          limits: flavorLimits
        })
      });
      const j: RunVerdict = await r.json();
      setRunVerdict(j);
    } catch (e: any) {
      setRunVerdict({ status: "ERR", message: e?.message ?? "network error" });
    } finally {
      setRunning(false);
    }
  }

  const oracleSrc = problem.sources.find((s) => s.lang === lang) ?? problem.sources[0];
  const disabled = submitting || !ready || !profile;
  const runDisabled = running || submitting;

  return (
    <>
      <CaptureAnimation event={capture} onDone={() => setCapture(null)} />
      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <label className="text-xs text-zinc-400">언어</label>
            <select
              className="rounded-md bg-zinc-800 px-2 py-1 text-sm"
              value={lang}
              onChange={(e) => onLangChange(e.target.value as Source["lang"])}
            >
              {langs.map((l) => <option key={l} value={l}>{l}</option>)}
            </select>
            <button
              className="ml-auto rounded-md bg-amber-500 px-3 py-1.5 text-sm font-bold text-zinc-900 hover:bg-amber-400 disabled:opacity-50"
              disabled={disabled}
              onClick={submit}
              title={!profile ? "먼저 트레이너를 등록하세요" : ""}
            >
              {submitting ? "전투 중..." : "⚔️ 도전!"}
            </button>
          </div>
          <div className="flex justify-between text-[11px] text-zinc-500">
            <span>{draftStatus === "loaded" ? "저장된 코드를 불러왔습니다." : draftStatus === "saved" ? "자동 저장됨" : "새 풀이"}</span>
            <span>Ctrl/Cmd + Enter 제출</span>
          </div>
          <div className="overflow-hidden rounded-xl border border-white/10">
            <Editor
              height="520px"
              theme="vs-dark"
              language={lang === "cpp" ? "cpp" : lang}
              value={code}
              onChange={(v) => setCode(v ?? "")}
              options={{ minimap: { enabled: false }, fontSize: 14, tabSize: 4 }}
              onMount={(editor, monaco) => {
                editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
                  submitRef.current();
                });
              }}
            />
          </div>
          <div className="rounded-xl border border-white/10 bg-zinc-900/60 p-3">
            <div className="mb-2 flex items-center gap-2">
              <label className="text-xs font-semibold text-zinc-300">직접 실행 입력</label>
              <button
                className="ml-auto rounded-md bg-zinc-700 px-3 py-1.5 text-xs font-bold text-zinc-100 hover:bg-zinc-600 disabled:opacity-50"
                disabled={runDisabled}
                onClick={runCustomInput}
              >
                {running ? "실행 중..." : "실행"}
              </button>
            </div>
            <textarea
              className="h-28 w-full resize-y rounded-lg border border-white/10 bg-black/30 p-2 font-mono text-xs text-zinc-100 outline-none focus:border-amber-400"
              value={customInput}
              onChange={(e) => setCustomInput(e.target.value)}
              spellCheck={false}
              placeholder="여기에 직접 테스트할 입력을 넣으세요."
            />
          </div>
          <button
            className="text-xs text-zinc-400 hover:text-white"
            onClick={() => setShowOracle((v) => !v)}
          >
            {showOracle ? "▼" : "▶"} 정답(Oracle) 코드 {showOracle ? "숨기기" : "보기"}
          </button>
          {showOracle && oracleSrc && (
            <pre className="max-h-72 overflow-auto rounded-xl border border-white/10 bg-black/50 p-3 text-xs">
              <code>{oracleSrc.code}</code>
            </pre>
          )}
        </div>

        <div className="space-y-3">
          <RunPanel result={runVerdict} />
          <VerdictPanel verdict={verdict} />
        </div>
      </div>
    </>
  );
}

function RunPanel({ result }: { result: RunVerdict | null }) {
  if (!result) {
    return (
      <div className="rounded-xl border border-dashed border-white/15 p-4 text-sm text-zinc-400">
        직접 실행 결과가 없습니다.
      </div>
    );
  }
  const style: Record<RunStatus, { bg: string; label: string }> = {
    OK: { bg: "bg-emerald-500", label: "실행 완료" },
    TLE: { bg: "bg-amber-500", label: "시간 초과" },
    MLE: { bg: "bg-orange-600", label: "메모리 초과" },
    RE: { bg: "bg-fuchsia-600", label: "런타임 에러" },
    CE: { bg: "bg-zinc-600", label: "컴파일 에러" },
    ERR: { bg: "bg-red-700", label: "실행기 오류" }
  };
  const s = style[result.status] ?? style.ERR;
  return (
    <div className="rounded-xl border border-white/10 bg-zinc-900 p-4">
      <div className="flex items-center gap-3">
        <span className={`pill text-white ${s.bg}`}>{result.status}</span>
        <span className="text-sm font-bold text-zinc-100">{s.label}</span>
        {result.durationMs != null && (
          <span className="ml-auto text-xs text-zinc-500">{result.durationMs} ms</span>
        )}
      </div>
      {result.message && (
        <pre className="mt-3 max-h-32 overflow-auto rounded-lg bg-black/50 p-3 text-xs text-rose-300">
          {result.message}
        </pre>
      )}
      <div className="mt-3 grid grid-cols-1 gap-2 md:grid-cols-2">
        <div>
          <div className="mb-1 text-[10px] text-zinc-500">stdout</div>
          <pre className="min-h-20 max-h-56 overflow-auto rounded bg-black/40 p-2 font-mono text-xs text-zinc-100">
            {result.stdout || ""}
          </pre>
        </div>
        <div>
          <div className="mb-1 text-[10px] text-zinc-500">stderr</div>
          <pre className="min-h-20 max-h-56 overflow-auto rounded bg-black/40 p-2 font-mono text-xs text-rose-200">
            {result.stderr || ""}
          </pre>
        </div>
      </div>
    </div>
  );
}

function VerdictPanel({ verdict }: { verdict: JudgeVerdict | null }) {
  if (!verdict) {
    return (
      <div className="rounded-xl border border-dashed border-white/15 p-6 text-center text-sm text-zinc-400">
        아직 도전 기록이 없습니다.<br />
        <span className="text-xs text-zinc-500">
          하네스가 입력 케이스를 자동 생성하여 Oracle 출력과 비교합니다.
        </span>
      </div>
    );
  }
  const STATUS_STYLE: Record<JudgeStatus, { bg: string; label: string; emoji: string }> = {
    AC:  { bg: "bg-emerald-500",        label: "맞았습니다!!", emoji: "\uD83C\uDFC6" },
    WA:  { bg: "bg-rose-500",           label: "틀렸습니다",   emoji: "\u274C"   },
    TLE: { bg: "bg-amber-500",          label: "시간 초과",    emoji: "\u23F1\uFE0F" },
    MLE: { bg: "bg-orange-600",         label: "메모리 초과",  emoji: "\uD83E\uDDE0" },
    RE:  { bg: "bg-fuchsia-600",        label: "런타임 에러",  emoji: "\uD83D\uDCA5" },
    CE:  { bg: "bg-zinc-600",           label: "컴파일 에러",  emoji: "\u26A0\uFE0F" },
    ERR: { bg: "bg-red-700",            label: "채점기 오류",  emoji: "\uD83D\uDED1" }
  };
  const sty = STATUS_STYLE[verdict.status as JudgeStatus] ?? STATUS_STYLE.ERR;
  return (
    <div className="rounded-xl border border-white/10 bg-zinc-900 p-4">
      <div className="flex items-center gap-3">
        <span className={`pill text-white ${sty.bg}`}>{sty.emoji} {verdict.status}</span>
        <span className="text-sm font-bold text-zinc-100">{sty.label}</span>
        {"passed" in verdict && (
          <span className="text-sm text-zinc-300">
            {verdict.passed} / {verdict.total} 통과
          </span>
        )}
        {"durationMs" in verdict && verdict.durationMs != null && (
          <span className="ml-auto text-xs text-zinc-500">{verdict.durationMs} ms</span>
        )}
      </div>
      {"message" in verdict && verdict.message && (
        <pre className="mt-3 max-h-40 overflow-auto rounded-lg bg-black/50 p-3 text-xs text-rose-300">
          {verdict.message}
        </pre>
      )}
      {"cases" in verdict && Array.isArray(verdict.cases) && (
        <ul className="mt-3 space-y-2">
          {verdict.cases.slice(0, 6).map((c) => {
            const v = c.verdict ?? (c.ok ? "AC" : "WA");
            const vColor: Record<string, string> = {
              AC: "text-emerald-400", WA: "text-rose-400",
              TLE: "text-amber-400", MLE: "text-orange-400", RE: "text-fuchsia-400"
            };
            return (
            <li key={c.idx} className="rounded-lg border border-white/5 bg-black/30 p-2">
              <div className="flex items-center gap-2 text-xs">
                <span className={vColor[v] ?? "text-zinc-300"}>
                  {c.ok ? "✓" : "✗"} {v}
                </span>
                <span className="text-zinc-400">case #{c.idx}</span>
                {c.duration_ms != null && (
                  <span className="text-[10px] text-zinc-500">{c.duration_ms}ms</span>
                )}
                <span className="ml-auto rounded bg-white/5 px-1.5 text-[10px] text-zinc-400">
                  {c.kind}
                </span>
              </div>
              {!c.ok && (
                <div className="mt-1 grid grid-cols-3 gap-2 font-mono text-[11px]">
                  <pre className="overflow-auto rounded bg-zinc-800 p-1">in:{"\n"}{c.input}</pre>
                  <pre className="overflow-auto rounded bg-zinc-800 p-1">expected:{"\n"}{c.expected}</pre>
                  <pre className="overflow-auto rounded bg-zinc-800 p-1">actual:{"\n"}{c.actual}</pre>
                </div>
              )}
            </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}
