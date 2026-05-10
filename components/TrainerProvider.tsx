"use client";

// 트레이너 프로필 (서버 백엔드 — SQLite + 쿠키 세션).
// 기존 컴포넌트 호환을 위해 TrainerProfile 형태를 그대로 유지한다.

import { createContext, useCallback, useContext, useEffect, useMemo, useState } from "react";
import type { RatingDelta } from "@/lib/rating";

export type CaptureRecord = {
  problemSlug: string;
  capturedAt: number;
  attempts: number;
  trAtCapture: number;
};

export type HistoryEntry = RatingDelta & { problemSlug?: string };

export type SubmissionEntry = {
  id: number;
  problemSlug: string;
  lang: string;
  status: string;
  passed: number | null;
  total: number | null;
  failedCaseKind: string | null;
  failedCaseVerdict: string | null;
  durationMs: number | null;
  codeBytes: number;
  ts: number;
};

export type TrainerProfile = {
  name: string;
  createdAt: number;
  tr: number;
  captures: Record<string, CaptureRecord>;
  attempts: Record<string, number>;
  history: HistoryEntry[];
  submissions: SubmissionEntry[];
};

type Ctx = {
  profile: TrainerProfile | null;
  ready: boolean;
  needsOnboarding: boolean;
  createTrainer: (name: string) => Promise<void>;
  resetTrainer: () => Promise<void>;
  bumpAttempt: (problemSlug: string) => void;
  applyWin: (problemSlug: string, delta: RatingDelta) => Promise<{ firstCapture: boolean }>;
  applyLoss: (problemSlug: string, delta: RatingDelta) => Promise<void>;
};

const TrainerCtx = createContext<Ctx | null>(null);

type ServerSnapshot = {
  trainer: { id: number; name: string; tr: number; dexCount: number; createdAt: number } | null;
  attempts?: Record<string, number>;
  captures?: { problemSlug: string; capturedAt: number; attemptsAtCapture: number; trAtCapture: number }[];
  history?: { id: number; problemSlug: string; problemR: number; expected: number; k: number; delta: number; prevTR: number; nextTR: number; outcome: "win" | "loss"; ts: number }[];
  submissions?: SubmissionEntry[];
};

function toProfile(s: ServerSnapshot): TrainerProfile | null {
  if (!s.trainer) return null;
  const captures: Record<string, CaptureRecord> = {};
  for (const c of s.captures ?? []) {
    captures[c.problemSlug] = {
      problemSlug: c.problemSlug,
      capturedAt: c.capturedAt,
      attempts: c.attemptsAtCapture,
      trAtCapture: c.trAtCapture
    };
  }
  const history: HistoryEntry[] = (s.history ?? []).map(h => ({
    problemSlug: h.problemSlug,
    problemR: h.problemR,
    expected: h.expected,
    k: h.k,
    delta: h.delta,
    prevTR: h.prevTR,
    nextTR: h.nextTR,
    outcome: h.outcome === "win" ? "win" : "lose"
  }));
  return {
    name: s.trainer.name,
    createdAt: s.trainer.createdAt,
    tr: s.trainer.tr,
    captures,
    attempts: s.attempts ?? {},
    history,
    submissions: s.submissions ?? []
  };
}

export function TrainerProvider({ children }: { children: React.ReactNode }) {
  const [profile, setProfile] = useState<TrainerProfile | null>(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    (async () => {
      try {
        const r = await fetch("/api/trainer", { cache: "no-store" });
        const j: ServerSnapshot = await r.json();
        setProfile(toProfile(j));
      } catch { /* ignore */ }
      setReady(true);
    })();
  }, []);

  const createTrainer = useCallback(async (name: string) => {
    const r = await fetch("/api/trainer", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ name })
    });
    if (!r.ok) {
      const j = await r.json().catch(() => ({}));
      throw new Error(j?.error ?? "트레이너 생성 실패");
    }
    const j: ServerSnapshot = await r.json();
    setProfile(toProfile(j));
  }, []);

  const resetTrainer = useCallback(async () => {
    await fetch("/api/trainer", { method: "DELETE" });
    setProfile(null);
  }, []);

  const bumpAttempt = useCallback((problemSlug: string) => {
    setProfile((cur) => {
      if (!cur) return cur;
      return {
        ...cur,
        attempts: { ...cur.attempts, [problemSlug]: (cur.attempts[problemSlug] ?? 0) + 1 }
      };
    });
    fetch("/api/trainer/attempt", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ problemSlug })
    }).catch(() => {});
  }, []);

  const applyWin = useCallback(async (problemSlug: string, delta: RatingDelta) => {
    setProfile((cur) => {
      if (!cur) return cur;
      const had = !!cur.captures[problemSlug];
      return {
        ...cur,
        tr: delta.nextTR,
        captures: had ? cur.captures : {
          ...cur.captures,
          [problemSlug]: {
            problemSlug,
            capturedAt: Date.now(),
            attempts: cur.attempts[problemSlug] ?? 1,
            trAtCapture: delta.nextTR
          }
        },
        history: [{ problemSlug, ...delta }, ...cur.history].slice(0, 50)
      };
    });
    const r = await fetch("/api/trainer/outcome", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        problemSlug,
        problemR: delta.problemR,
        expected: delta.expected,
        k: delta.k,
        delta: delta.delta,
        prevTR: delta.prevTR,
        nextTR: delta.nextTR,
        outcome: "win"
      })
    });
    if (!r.ok) return { firstCapture: false };
    const j = await r.json();
    return { firstCapture: !!j.firstCapture };
  }, []);

  const applyLoss = useCallback(async (problemSlug: string, delta: RatingDelta) => {
    setProfile((cur) => {
      if (!cur) return cur;
      return {
        ...cur,
        tr: delta.nextTR,
        history: [{ problemSlug, ...delta }, ...cur.history].slice(0, 50)
      };
    });
    await fetch("/api/trainer/outcome", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        problemSlug,
        problemR: delta.problemR,
        expected: delta.expected,
        k: delta.k,
        delta: delta.delta,
        prevTR: delta.prevTR,
        nextTR: delta.nextTR,
        outcome: "loss"
      })
    }).catch(() => {});
  }, []);

  const value = useMemo<Ctx>(() => ({
    profile, ready,
    needsOnboarding: ready && profile === null,
    createTrainer, resetTrainer, bumpAttempt, applyWin, applyLoss
  }), [profile, ready, createTrainer, resetTrainer, bumpAttempt, applyWin, applyLoss]);

  return <TrainerCtx.Provider value={value}>{children}</TrainerCtx.Provider>;
}

export function useTrainer(): Ctx {
  const v = useContext(TrainerCtx);
  if (!v) throw new Error("useTrainer must be used within TrainerProvider");
  return v;
}
