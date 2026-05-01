// 트레이너 프로필 (localStorage 단일 유저).
// SSR 안전 가드 포함.

import type { RatingDelta } from "./rating";

const KEY = "dongjun.codedex.trainer.v1";
const STARTING_TR = 1000;

export type CaptureRecord = {
  problemSlug: string;
  capturedAt: number;
  attempts: number;
  trAtCapture: number;
};

export type TrainerProfile = {
  name: string;
  createdAt: number;
  tr: number;
  captures: Record<string, CaptureRecord>;   // problemSlug -> record
  attempts: Record<string, number>;          // problemSlug -> attempts (성공 포함)
  history: RatingDelta[];                    // 최근 50개
};

export function emptyProfile(name: string): TrainerProfile {
  return {
    name: name.trim() || "이름없음",
    createdAt: Date.now(),
    tr: STARTING_TR,
    captures: {},
    attempts: {},
    history: []
  };
}

export function loadProfile(): TrainerProfile | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = window.localStorage.getItem(KEY);
    if (!raw) return null;
    const p = JSON.parse(raw) as TrainerProfile;
    // 마이그레이션 가드
    if (typeof p?.tr !== "number" || !p.captures) return null;
    return p;
  } catch {
    return null;
  }
}

export function saveProfile(p: TrainerProfile) {
  if (typeof window === "undefined") return;
  window.localStorage.setItem(KEY, JSON.stringify(p));
}

export function resetProfile() {
  if (typeof window === "undefined") return;
  window.localStorage.removeItem(KEY);
}

// 시도 기록 (AC/WA 무관) — 다음 도전의 K-factor 계산용
export function bumpAttempt(p: TrainerProfile, problemSlug: string): TrainerProfile {
  const next = { ...p, attempts: { ...p.attempts } };
  next.attempts[problemSlug] = (next.attempts[problemSlug] ?? 0) + 1;
  return next;
}

// 캡처 등록 — 이미 잡았으면 그대로 둠 (재AC는 TR 변동 X)
export function captureMonster(
  p: TrainerProfile,
  opts: { problemSlug: string; delta: import("./rating").RatingDelta }
): { profile: TrainerProfile; firstCapture: boolean } {
  if (p.captures[opts.problemSlug]) {
    return { profile: p, firstCapture: false };
  }
  const profile: TrainerProfile = {
    ...p,
    tr: opts.delta.nextTR,
    captures: {
      ...p.captures,
      [opts.problemSlug]: {
        problemSlug: opts.problemSlug,
        capturedAt: Date.now(),
        attempts: p.attempts[opts.problemSlug] ?? 1,
        trAtCapture: opts.delta.nextTR
      }
    },
    history: [opts.delta, ...p.history].slice(0, 50)
  };
  return { profile, firstCapture: true };
}

// 패배(WA/RE/TLE) — TR 살짝 하락만, 캡처는 X
export function recordLoss(
  p: TrainerProfile,
  delta: RatingDelta
): TrainerProfile {
  return {
    ...p,
    tr: delta.nextTR,
    history: [delta, ...p.history].slice(0, 50)
  };
}

export function dexCount(p: TrainerProfile): number {
  return Object.keys(p.captures).length;
}
