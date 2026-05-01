// 포켓몬 테마 문제 본문 합성기.
//
// 입력:
//   - problem (BOJ id, slug, category, oracle code)
//   - meta    (solved.ac titleKo, level, levelName, tags)
//   - monster (실제 포켓몬: name, types, rarity)
// 출력:
//   FlavorProblem {
//     subject:    "포켓몬 시나리오 한 줄"
//     situation:  "마크다운 본문 (세팅, 미션, 제약)"
//     inputSpec:  "포켓몬 용어로 바꾼 입력 형식"
//     outputSpec: "포켓몬 용어로 바꾼 출력 형식"
//     samples:    [{in, out, explain}]
//     limits:     { timeLimitMs, memoryLimitMb }   // 메타에서 추정
//   }
//
// 전략:
//   - 같은 입력 = 같은 결과 (해시 시드)
//   - 카테고리별 시나리오 템플릿 (그리디=배지수집, DP=진화경로, 그래프=마을이동...)
//   - 태그가 있으면 더 구체적 변형
//   - Oracle 코드를 정적으로 파싱해 "정수 N개 입력" 같은 IO 패턴 추출
//   - 인기 문제(예: 1000, 2798)는 수동 오버라이드(harness/overrides 와 별개)

import type { Problem } from "./types";
import type { MonsterMapEntry } from "./characters";
import { getStatement, type ProblemStatement } from "./statement";
import { adaptForPokemon } from "./adapt";

export type FlavorSample = { in: string; out: string; explain?: string };

export type FlavorProblem = {
  subject: string;
  situation: string;
  inputSpec: string;
  outputSpec: string;
  samples: FlavorSample[];
  limits: { timeLimitMs: number; memoryLimitMb: number };
  bojTitle?: string;
  bojLink?: string;
  source: "boj" | "synthesized";
  hint?: string;
  limitText?: string;
  snapshotTs?: string;
  /** BOJ 원문이 있을 경우, 각색되지 않은 원문 (토글 표시용) */
  raw?: { description: string; input: string; output: string };
};

export type ProblemMeta = {
  titleKo: string;
  level: number;
  levelName: string;
  tags: { key: string; name_ko: string }[];
  acceptedCount: number;
  averageTries: number;
};

// ----- 결정적 PRNG -----
function rng(seed: string) {
  let h = 2166136261;
  for (let i = 0; i < seed.length; i++) {
    h ^= seed.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  let s = h >>> 0;
  return () => {
    s |= 0; s = (s + 0x6D2B79F5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const pick = <T>(r: () => number, arr: T[]) => arr[Math.floor(r() * arr.length)]!;

// ----- 시간/메모리 제한 추정 (티어 기반) -----
function estimateLimits(level: number) {
  // BOJ 평균 기준 휴리스틱
  if (level >= 21) return { timeLimitMs: 3000, memoryLimitMb: 512 };  // Diamond+
  if (level >= 16) return { timeLimitMs: 2000, memoryLimitMb: 512 };
  if (level >= 11) return { timeLimitMs: 2000, memoryLimitMb: 256 };
  if (level >= 6)  return { timeLimitMs: 2000, memoryLimitMb: 256 };
  return { timeLimitMs: 2000, memoryLimitMb: 256 };
}

// ----- Oracle 코드에서 IO 패턴 가볍게 추정 -----
type IOHint = "single_int" | "two_ints" | "array_n" | "nm_array" | "grid" | "string" | "graph" | "unknown";

function detectIO(code: string, categorySlug: string): IOHint {
  const c = code.replace(/\s+/g, " ");
  // 수동 카테고리 우선
  if (categorySlug === "graph_traversal" || categorySlug === "shortest_path"
   || categorySlug === "minimum_spanning_tree" || categorySlug === "tree"
   || categorySlug === "disjoint_set" || categorySlug === "dynamic_programming_on_trees")
    return "graph";
  if (categorySlug === "string" || categorySlug === "trie") return "string";
  if (categorySlug === "simulation") return "grid";
  // 코드 휴리스틱
  if (/N,\s*M\s*=\s*map\(int/.test(c) || /int\s+N,\s*M/.test(c)) return "nm_array";
  if (/N\s*=\s*int\(input/.test(c))  return "array_n";
  if (/A,\s*B\s*=\s*map\(int/.test(c)) return "two_ints";
  if (/int\s+\w+\s*=\s*int\(input/.test(c)) return "single_int";
  return "unknown";
}

// ----- 카테고리별 포켓몬 시나리오 템플릿 -----
// 모든 함수: (rng, monster, meta, hint) => 스토리 객체

type StoryCtx = {
  r: () => number;
  monster: MonsterMapEntry;
  meta?: ProblemMeta;
  hint: IOHint;
  problem: Problem;
};

const TRAINER_NAMES = ["지우", "이슬", "웅이", "로켓단", "오박사", "그린", "단풍", "민들레", "초롱", "별이"];
const TOWNS = ["태초마을", "상록시티", "회색시티", "노랑시티", "파도시티", "보라타운", "셀레비숲", "호연시티"];

function story_brute_force(ctx: StoryCtx) {
  const { r, monster, problem } = ctx;
  const trainer = pick(r, TRAINER_NAMES);
  const town = pick(r, TOWNS);
  const subject = `🎴 ${trainer}와 ${monster.ko}의 카드 챌린지`;
  const situation =
`**${town}** 의 게임 코너에서 ${monster.ko}가 트레이너 **${trainer}** 에게 카드 게임을 제안했다.\n\n` +
`테이블 위에 놓인 카드 N장 중 정확히 **3장** 을 골라 합을 만든다.\n` +
`이 합이 ${monster.ko}가 정한 한도 M을 넘지 않으면서 가장 큰 값이 되도록 하라.\n\n` +
`> 💡 모든 가능한 3장의 조합을 시도해야 한다 — **완전탐색** 의 정수.`;
  const inputSpec  = "첫 줄: 카드 수 **N**, 한도 **M** (공백 구분)\n둘째 줄: N개 카드의 정수 값";
  const outputSpec = "조건을 만족하는 합 중 최대값";
  const samples: FlavorSample[] = [
    { in: "5 21\n5 6 7 8 9", out: "21", explain: "6+7+8 = 21 (정확히 한도)" },
    { in: "10 500\n93 181 245 214 315 36 185 138 216 295", out: "479" }
  ];
  return { subject, situation, inputSpec, outputSpec, samples };
}

function story_math(ctx: StoryCtx) {
  const { r, monster, problem } = ctx;
  const t = pick(r, TRAINER_NAMES);
  const subject = `🔢 ${monster.ko}의 수학 도장`;
  const situation =
`수학 타입의 야생 ${monster.ko}이(가) ${t}의 앞을 막아섰다.\n\n` +
`"이 수식을 정확히 풀면 길을 비켜주마." — ${monster.ko}\n\n` +
`주어진 입력으로 정확한 정수/실수를 계산해 출력하라. ` +
`수학 공식 또는 모듈러 산술이 핵심이다.`;
  const inputSpec  = "문제 정의에 따른 정수 입력";
  const outputSpec = "계산 결과 한 줄";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

function story_dp(ctx: StoryCtx) {
  const { r, monster, problem } = ctx;
  const t = pick(r, TRAINER_NAMES);
  const subject = `🧬 ${monster.ko}의 진화 경로 최적화`;
  const situation =
`${t}의 ${monster.ko}는 N단계의 진화 트리를 가진다. ` +
`각 단계에서 선택한 진화 경로의 비용/가치가 누적되며, 최적의 누적값을 구해야 한다.\n\n` +
`> 🧠 작은 부분문제의 최적해를 결합해 큰 문제를 푼다 — **동적 계획법**.\n` +
`> 이전 상태를 어떻게 정의하고 전이할지가 관건.`;
  const inputSpec  = "단계 수 N (그리고 추가 파라미터)";
  const outputSpec = "DP 테이블 최종값";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

function story_graph(ctx: StoryCtx) {
  const { r, monster } = ctx;
  const t = pick(r, TRAINER_NAMES);
  const start = pick(r, TOWNS), end = pick(r, TOWNS);
  const subject = `🗺️ ${start} → ${end} : ${monster.ko}의 길찾기`;
  const situation =
`${t}는 ${start}에서 ${end}로 ${monster.ko}와 함께 이동해야 한다.\n` +
`마을들은 정점, 길은 간선으로 표현된다. N개의 정점과 M개의 간선이 주어진다.\n\n` +
`> 🛤️ 모든 도달 가능한 마을을 BFS/DFS로 탐색하거나, 최적 경로를 찾는다.`;
  const inputSpec  = "첫 줄: 정점 수 **N**, 간선 수 **M**\n다음 M줄: 양 끝 정점 a b";
  const outputSpec = "탐색/거리 결과";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

function story_shortest_path(ctx: StoryCtx) {
  const s = story_graph(ctx);
  return {
    ...s,
    subject: `⚡ ${ctx.monster.ko}의 최단경로 — ` + s.subject.replace(/^🗺️\s*/, ""),
    situation: s.situation +
      `\n\n> 💎 다익스트라/벨만-포드/플로이드-워셜 중 어떤 것이 적합한지 판단하라.`
  };
}

function story_greedy(ctx: StoryCtx) {
  const { r, monster } = ctx;
  const t = pick(r, TRAINER_NAMES);
  const subject = `🍃 ${monster.ko}의 배지 수집 전략`;
  const situation =
`${t}는 N개의 체육관을 돌며 배지를 모은다. ` +
`각 체육관은 도전 시간/보상이 다르며, 매 순간 **가장 이득이 큰 선택** 을 해야 최적이다.\n\n` +
`> 💰 정렬 + 우선순위 큐가 자주 쓰인다 — **그리디**.`;
  const inputSpec  = "체육관 수 N, 각각의 파라미터";
  const outputSpec = "최대 배지 수 또는 누적 보상";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

function story_simulation(ctx: StoryCtx) {
  const { r, monster } = ctx;
  const subject = `🎮 ${monster.ko}의 NxM 미로 시뮬레이션`;
  const situation =
`N×M 격자 던전에서 ${monster.ko}가 정해진 규칙대로 움직인다.\n` +
`주어진 명령을 순서대로 정확히 시뮬레이션하라.\n\n` +
`> 🧭 사방/팔방 좌표 변환과 경계 체크를 깔끔하게 짜는 것이 핵심.`;
  const inputSpec  = "격자 크기 N M, 격자 내용, 명령 시퀀스";
  const outputSpec = "최종 상태 또는 누적 통계";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

function story_string(ctx: StoryCtx) {
  const { r, monster } = ctx;
  const subject = `📜 ${monster.ko}의 비밀 두루마리`;
  const situation =
`${monster.ko}가 들고 있는 두루마리에는 알 수 없는 문자열이 적혀있다.\n` +
`주어진 패턴/조건에 맞게 가공하거나 검색하라.`;
  const inputSpec  = "문자열 (또는 여러 줄)";
  const outputSpec = "변환/검색 결과";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

function story_implementation(ctx: StoryCtx) {
  const { monster } = ctx;
  const subject = `🛠️ ${monster.ko}의 정확한 절차 구현`;
  const situation =
`${monster.ko}의 의식은 명세대로 한 단계 한 단계 정확히 수행되어야 한다. ` +
`자료구조 선택보다 **명세를 정확히 코드로 옮기는 능력** 이 핵심.`;
  const inputSpec  = "명세에 정의된 입력";
  const outputSpec = "절차의 결과";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

function story_default(ctx: StoryCtx) {
  const { monster, meta } = ctx;
  const subject = `🌀 ${monster.ko}의 ${meta?.titleKo ?? "도전"}`;
  const situation =
`야생의 ${monster.ko}이(가) 도전장을 던졌다.\n\n` +
`> 카테고리: ${meta?.tags?.map(t => "`" + t.name_ko + "`").join(", ") || "—"}\n` +
`> 난이도: ${meta?.levelName ?? "—"}`;
  const inputSpec  = "표준입력 (BOJ 원문 참고)";
  const outputSpec = "표준출력";
  return { subject, situation, inputSpec, outputSpec, samples: [] };
}

const STORY_BY_CATEGORY: Record<string, (ctx: StoryCtx) => any> = {
  brute_force: story_brute_force,
  backtracking: story_brute_force,
  math: story_math,
  dynamic_programming_1: story_dp,
  dynamic_programming_2: story_dp,
  dynamic_programming_on_trees: story_dp,
  graph_traversal: story_graph,
  tree: story_graph,
  trie: story_string,
  disjoint_set: story_graph,
  shortest_path: story_shortest_path,
  minimum_spanning_tree: story_shortest_path,
  greedy: story_greedy,
  simulation: story_simulation,
  string: story_string,
  implementation: story_implementation,
  prefix_sum: story_implementation,
  two_pointer: story_implementation,
  binary_search: story_implementation,
  data_structure: story_implementation,
  data_structure2: story_implementation,
  divide_and_conquer: story_dp
};

// ----- 수동 오버라이드 (인기 문제용) -----
const OVERRIDES: Record<string, Partial<FlavorProblem>> = {
  // 1000번 (A+B)
  "math-1000": {
    subject: "🥚 알주머니의 수학 — 두 수의 합",
    situation:
`코코몽이 둘로 갈라진 알주머니에서 두 마리의 어린 포켓몬이 나왔다.\n` +
`각 알주머니의 무게 **A** 와 **B** 가 주어질 때, 둘을 합한 무게를 구하라.`,
    inputSpec: "공백으로 구분된 두 정수 A B (1 ≤ A, B ≤ 10)",
    outputSpec: "A + B",
    samples: [{ in: "1 2", out: "3" }]
  }
};

export function buildFlavor(
  problem: Problem,
  monster: MonsterMapEntry,
  meta: ProblemMeta | undefined
): FlavorProblem {
  const bojLink = problem.link ?? `https://www.acmicpc.net/problem/${problem.id}`;

  // 1) BOJ 원문 (Wayback) 이 있으면 → 포켓몬으로 각색
  const stmt = getStatement(problem.id);
  if (stmt) {
    const adapted = adaptForPokemon(problem, monster, {
      description: stmt.description,
      input:       stmt.input,
      output:      stmt.output
    });
    const limits = {
      timeLimitMs:  stmt.limits.timeLimitMs  ?? estimateLimits(meta?.level ?? 0).timeLimitMs,
      memoryLimitMb: stmt.limits.memoryLimitMb ?? estimateLimits(meta?.level ?? 0).memoryLimitMb
    };
    return {
      subject:    `📖 ${stmt.title} — ${monster.ko} 의 도전`,
      situation:  `${adapted.intro}\n\n${adapted.description}`,
      inputSpec:  adapted.input  || "표준 입력",
      outputSpec: adapted.output || "표준 출력",
      samples:    stmt.samples.map(s => ({ in: s.in, out: s.out })),
      limits,
      bojTitle:   stmt.title,
      bojLink,
      source:     "boj",
      hint:       stmt.hint,
      limitText:  stmt.limit,
      snapshotTs: stmt.snapshotTs,
      raw: {
        description: stmt.description,
        input:       stmt.input,
        output:      stmt.output
      }
    };
  }

  // 2) 합성 fallback
  const r = rng(`flavor:${problem.slug}:${monster.no}`);
  const oracle = problem.sources[0]?.code ?? "";
  const hint = detectIO(oracle, problem.categorySlug);
  const ctx: StoryCtx = { r, monster, meta, hint, problem };
  const builder = STORY_BY_CATEGORY[problem.categorySlug] ?? story_default;
  const base = builder(ctx);
  const limits = estimateLimits(meta?.level ?? 0);

  const out: FlavorProblem = {
    subject:    base.subject,
    situation:  base.situation,
    inputSpec:  base.inputSpec,
    outputSpec: base.outputSpec,
    samples:    base.samples ?? [],
    limits,
    bojTitle:   meta?.titleKo,
    bojLink,
    source:     "synthesized"
  };
  const ov = OVERRIDES[problem.slug];
  if (ov) Object.assign(out, ov);
  return out;
}
