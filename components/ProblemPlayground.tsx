"use client";

import dynamic from "next/dynamic";
import { useState } from "react";
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
  const [verdict, setVerdict] = useState<JudgeVerdict | null>(null);
  const [showOracle, setShowOracle] = useState(false);
  const [capture, setCapture] = useState<CaptureEvent | null>(null);

  const { profile, ready, applyWin, applyLoss, bumpAttempt } = useTrainer();

  function onLangChange(next: Source["lang"]) {
    setLang(next);
    setCode(STARTER[next] ?? "");
  }

  async function submit() {
    if (!ready || !profile) return;
    setSubmitting(true); setVerdict(null);

    bumpAttempt(problem.slug);
    const attemptsBefore = (profile.attempts[problem.slug] ?? 0) + 1;

    try {
      const monsterEntry = getMonsterEntry(problem.slug);
      const flavor = monsterEntry
        ? buildFlavor(problem, monsterEntry, getProblemMeta(problem.id))
        : null;
      const r = await fetch("/api/judge", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          problemSlug: problem.slug, lang, code,
          limits: flavor?.limits
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

  const oracleSrc = problem.sources.find((s) => s.lang === lang) ?? problem.sources[0];
  const disabled = submitting || !ready || !profile;

  return (
    <>
      <CaptureAnimation event={capture} onDone={() => setCapture(null)} />
      <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <label className="text-xs text-white/40">언어</label>
            <select
              className="rounded-lg border border-white/[0.06] bg-white/[0.05] px-3 py-1.5 text-sm"
              value={lang}
              onChange={(e) => onLangChange(e.target.value as Source["lang"])}
            >
              {langs.map((l) => <option key={l} value={l}>{l}</option>)}
            </select>
            <button
              className="btn-primary ml-auto disabled:opacity-40"
              disabled={disabled}
              onClick={submit}
              title={!profile ? "먼저 트레이너를 등록하세요" : ""}
            >
              {submitting ? "전투 중... ⚔️" : "도전하기 ⚔️"}
            </button>
          </div>
          <div className="overflow-hidden rounded-xl border border-white/[0.06]">
            <Editor
              height="520px"
              theme="vs-dark"
              language={lang === "cpp" ? "cpp" : lang}
              value={code}
              onChange={(v) => setCode(v ?? "")}
              options={{ minimap: { enabled: false }, fontSize: 14, tabSize: 4 }}
            />
          </div>
          <button
            className="text-xs text-white/40 transition-colors hover:text-amber-300"
            onClick={() => setShowOracle((v) => !v)}
          >
            {showOracle ? "▼" : "▶"} 정답 코드 {showOracle ? "숨기기" : "보기"}
          </button>
          {showOracle && oracleSrc && (
            <pre className="max-h-72 overflow-auto rounded-xl border border-white/[0.06] bg-black/30 p-3 text-xs">
              <code>{oracleSrc.code}</code>
            </pre>
          )}
        </div>

        <div className="space-y-3">
          <VerdictPanel verdict={verdict} />
        </div>
      </div>
    </>
  );
}

function VerdictPanel({ verdict }: { verdict: JudgeVerdict | null }) {
  if (!verdict) {
    return (
      <div className="poke-card p-8 text-center">
        <span className="text-4xl">⚔️</span>
        <p className="mt-2 text-sm text-white/40">아직 도전 기록이 없어요</p>
        <p className="mt-1 text-xs text-white/20">
          코드를 작성하고 도전하면 자동으로 채점돼요!
        </p>
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
    <div className="poke-card p-4">
      <div className="flex items-center gap-3">
        <span className={`pill text-white ${sty.bg}`}>{sty.emoji} {verdict.status}</span>
        <span className="text-sm font-extrabold">{sty.label}</span>
        {"passed" in verdict && (
          <span className="text-sm text-white/50">
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
