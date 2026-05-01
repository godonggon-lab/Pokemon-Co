// 트레이너 레이팅(TR) 산정 시스템.
// 컨셉: ELO 변형 + 카테고리 가중 + 시도 횟수 K-factor.
//
// 입력:
//   problemId    : "1000" 같은 BOJ 번호 (자릿수 → 기본 난이도 베이스)
//   categorySlug : 카테고리 가중치 매핑
//   attempts     : 해당 문제에 누적 시도 횟수 (1 = 첫 풀이)
//
// 출력:
//   problemRating(R_p), expected(E), delta(ΔTR), nextTR

import type { Category } from "./types";

// 카테고리별 난이도 보정 (BOJ 체감 난이도 기반 휴리스틱)
const CATEGORY_BIAS: Record<string, number> = {
  brute_force:                   0,
  implementation:                0,
  math:                          20,
  string:                        30,
  greedy:                        40,
  prefix_sum:                    40,
  two_pointer:                   60,
  binary_search:                 60,
  data_structure:                70,
  data_structure2:               90,
  simulation:                    80,
  backtracking:                  90,
  graph_traversal:              100,
  divide_and_conquer:           110,
  disjoint_set:                 120,
  shortest_path:                130,
  tree:                         110,
  trie:                         120,
  dynamic_programming_1:        140,
  dynamic_programming_2:        170,
  dynamic_programming_on_trees: 180,
  minimum_spanning_tree:        150
};

export function problemRating(problemId: string, categorySlug: string): number {
  // 자릿수 베이스: 1자리 800, 2자리 900, ... 5자리 1200, 6자리 1300
  const digits = String(problemId).length;
  const base = 700 + Math.min(digits, 6) * 100;
  const bias = CATEGORY_BIAS[categorySlug] ?? 50;
  return base + bias;
}

export function expectedScore(traineRating: number, problemR: number): number {
  return 1 / (1 + Math.pow(10, (problemR - traineRating) / 400));
}

// 시도 횟수가 늘면 K가 줄어든다 (도전 가치 감소)
function kFactor(attempts: number): number {
  if (attempts <= 1) return 40;
  if (attempts <= 3) return 28;
  if (attempts <= 7) return 18;
  return 12;
}

export type RatingDelta = {
  problemR: number;
  expected: number;
  delta: number;       // 변동량 (양수=상승)
  prevTR: number;
  nextTR: number;
  k: number;
  outcome: "win" | "lose";
};

export function applyOutcome(opts: {
  prevTR: number;
  problemId: string;
  categorySlug: string;
  attempts: number;
  win: boolean;
}): RatingDelta {
  const R_p = problemRating(opts.problemId, opts.categorySlug);
  const E   = expectedScore(opts.prevTR, R_p);
  const k   = kFactor(opts.attempts);
  const score = opts.win ? 1 : 0;
  // 패배 시에도 손실은 절반 (학습 목적)
  const raw = k * (score - E);
  const delta = opts.win ? raw : raw * 0.5;
  const nextTR = Math.max(0, Math.round(opts.prevTR + delta));
  return {
    problemR: R_p,
    expected: E,
    delta: Math.round(delta * 10) / 10,
    prevTR: opts.prevTR,
    nextTR,
    k,
    outcome: opts.win ? "win" : "lose"
  };
}

// ---- 배지 등급 ----
export type Badge = {
  id: string;
  label: string;
  emoji: string;
  min: number;
  ringClass: string;
  textClass: string;
  bgClass: string;
};

export const BADGES: Badge[] = [
  { id: "rookie",   label: "새내기 트레이너", emoji: "🆕", min: 0,    ringClass: "ring-zinc-500",    textClass: "text-zinc-300", bgClass: "bg-zinc-700/40" },
  { id: "bronze",   label: "브론즈 배지",     emoji: "🥉", min: 800,  ringClass: "ring-amber-700",   textClass: "text-amber-300", bgClass: "bg-amber-900/30" },
  { id: "silver",   label: "실버 배지",       emoji: "🥈", min: 1000, ringClass: "ring-zinc-300",    textClass: "text-zinc-100",  bgClass: "bg-zinc-500/30" },
  { id: "gold",     label: "골드 배지",       emoji: "🥇", min: 1200, ringClass: "ring-amber-400",   textClass: "text-amber-300", bgClass: "bg-amber-500/20" },
  { id: "platinum", label: "플래티넘 배지",   emoji: "💎", min: 1400, ringClass: "ring-sky-300",     textClass: "text-sky-200",   bgClass: "bg-sky-500/20" },
  { id: "diamond",  label: "다이아 배지",     emoji: "💠", min: 1600, ringClass: "ring-cyan-400",    textClass: "text-cyan-200",  bgClass: "bg-cyan-500/20" },
  { id: "master",   label: "마스터볼",        emoji: "⚡", min: 1800, ringClass: "ring-violet-400",  textClass: "text-violet-200",bgClass: "bg-violet-500/20" },
  { id: "champion", label: "챔피언",          emoji: "👑", min: 2000, ringClass: "ring-rose-500",    textClass: "text-rose-200",  bgClass: "bg-rose-500/20" }
];

export function badgeOf(tr: number): Badge {
  let chosen = BADGES[0];
  for (const b of BADGES) if (tr >= b.min) chosen = b;
  return chosen;
}

export function nextBadge(tr: number): Badge | null {
  for (const b of BADGES) if (b.min > tr) return b;
  return null;
}
