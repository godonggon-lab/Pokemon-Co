// BOJ 원문을 포켓몬 세계관으로 각색하는 트랜스포머.
//
// 원칙:
//  - 숫자/제약/수식/입력형식은 절대 건드리지 않음 (정답성 유지)
//  - 인물·장소·사물 명사만 포켓몬 용어로 치환
//  - 인트로 한 단락 추가 ("야생의 OOO이(가) 도전장을!")
//  - 카테고리에 따라 다른 어휘 선택 (그래프=마을이동, DP=진화경로...)
//  - 결정적: 같은 (slug, monster) 입력은 항상 같은 출력

import type { MonsterMapEntry } from "./characters";
import type { Problem } from "./types";

// ---- 결정적 PRNG ----
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
const pick = <T>(r: () => number, arr: T[]): T => arr[Math.floor(r() * arr.length)]!;

// ---- 포켓몬 세계관 어휘 ----
const TRAINERS = ["지우", "이슬", "웅이", "한별", "그린", "단풍", "민들레", "초롱", "별이", "한솔"];
const TOWNS    = ["태초마을", "상록시티", "회색시티", "노랑시티", "보라타운", "셀레비숲", "호연시티", "성도지방", "전기마을"];
const PROFS    = ["오박사", "관박사", "느티나무박사", "삼나무박사"];

// ---- 카테고리별 모티프 ----
type Motif = {
  intro: (m: MonsterMapEntry, trainer: string, town: string) => string;
  // 명사 치환표 (단어 경계가 모호한 한국어이므로 보수적으로 골라야 함)
  replacements: Array<[RegExp, string | ((m: MonsterMapEntry) => string)]>;
};

function motifFor(categorySlug: string): Motif {
  const base: Motif = {
    intro: (m, t, town) =>
      `🎒 **${town}** 의 트레이너 **${t}** 는 야생의 **${m.ko}** 와 마주쳤다. ` +
      `${m.ko} 가 도전장을 내밀며 말한다 — *"이 시험을 통과하면 함께 가주마."* 🌟\n\n` +
      `> 다음은 ${m.ko} 가 건넨 도감 페이지의 내용이다.`,
    replacements: [
      // 보편적 인물 → 트레이너
      [/사람/g, "트레이너"],
      [/학생/g, "수련생"],
      [/선생님/g, "체육관 관장"],
      [/친구/g, "동료 트레이너"],
      [/도시/g, "마을"],
      [/마을/g, "포켓몬마을"], // 위가 먼저 적용됨
      [/학교/g, "포켓몬 학교"],
      [/회사/g, "포켓몬 길드"],
      [/카드/g, "배지카드"],
      [/돈/g,   "포켓머니"],
      [/물건/g, "도구"],
      [/책/g,   "도감"]
    ]
  };
  switch (categorySlug) {
    case "graph_traversal":
    case "shortest_path":
    case "minimum_spanning_tree":
    case "tree":
    case "disjoint_set":
      return {
        intro: (m, t, town) =>
          `🗺️ ${town} 에서 출발한 트레이너 **${t}** 와 ${m.ko} 가 미지의 지도를 건네받았다. ` +
          `정점은 마을, 간선은 길. 이 지도를 정복해야 다음 체육관에 닿는다.\n\n` +
          `> 다음은 지도와 함께 적힌 임무 내용이다.`,
        replacements: [
          ...base.replacements,
          [/노드/g, "마을"],
          [/정점/g, "마을"],
          [/간선/g, "길"]
        ]
      };
    case "dynamic_programming_1":
    case "dynamic_programming_2":
    case "dynamic_programming_on_trees":
      return {
        intro: (m, t, town) =>
          `🧬 진화 직전의 ${m.ko} 가 트레이너 **${t}** 에게 결단을 요구한다. ` +
          `이전 단계의 최적 선택이 다음 단계의 진화 경로를 결정짓는다.\n\n` +
          `> 다음은 진화 분기점에서 풀어야 할 문제이다.`,
        replacements: base.replacements
      };
    case "greedy":
      return {
        intro: (m, t, town) =>
          `🍃 트레이너 **${t}** 와 **${m.ko}** 는 한 정거장도 낭비할 수 없다. ` +
          `매 순간 가장 이득이 큰 선택만이 챔피언의 길로 인도한다.\n\n` +
          `> 다음은 길목에서 마주친 선택지이다.`,
        replacements: base.replacements
      };
    case "simulation":
    case "implementation":
      return {
        intro: (m, t, town) =>
          `🎮 ${m.ko} 가 트레이너 **${t}** 에게 정확한 절차를 요구한다. ` +
          `한 칸이라도 틀리면 환영의 미궁에 갇히게 된다.\n\n` +
          `> 다음은 ${m.ko} 가 건넨 절차서이다.`,
        replacements: base.replacements
      };
    case "string":
    case "trie":
      return {
        intro: (m, t, town) =>
          `📜 ${m.ko} 의 등에 새겨진 고대 문자가 트레이너 **${t}** 의 손에 들어왔다. ` +
          `풀어내야만 진화의 비밀이 열린다.\n\n` +
          `> 다음은 두루마리에 적힌 내용이다.`,
        replacements: base.replacements
      };
    case "math":
      return {
        intro: (m, t, town) =>
          `🔢 수학 타입의 야생 ${m.ko} 가 트레이너 **${t}** 의 길을 막아섰다. ` +
          `정확한 수식을 풀어야만 통과할 수 있다.\n\n` +
          `> 다음은 ${m.ko} 가 건넨 수식 문제이다.`,
        replacements: base.replacements
      };
    case "brute_force":
    case "backtracking":
      return {
        intro: (m, t, town) =>
          `🎴 ${m.ko} 가 트레이너 **${t}** 에게 모든 가능성을 시험할 것을 요구한다. ` +
          `숨겨진 답은 무수한 조합 속에 있다.\n\n` +
          `> 다음은 ${m.ko} 가 건넨 챌린지 카드의 내용이다.`,
        replacements: base.replacements
      };
    case "binary_search":
    case "two_pointer":
    case "prefix_sum":
      return {
        intro: (m, t, town) =>
          `⚡ ${m.ko} 가 광활한 범위에서 빠르게 답을 찾으라고 트레이너 **${t}** 에게 명한다.\n\n` +
          `> 다음은 시험의 내용이다.`,
        replacements: base.replacements
      };
    case "data_structure":
    case "data_structure2":
      return {
        intro: (m, t, town) =>
          `📦 트레이너 **${t}** 의 가방이 ${m.ko} 의 마법으로 한정된 도구만 허용한다. ` +
          `자료를 효율적으로 다루지 못하면 시간이 모자란다.\n\n` +
          `> 다음은 ${m.ko} 가 건넨 시험이다.`,
        replacements: base.replacements
      };
    default:
      return base;
  }
}

// ---- 사람 이름 같은 한국 인명 → 트레이너 이름으로 ----
// 너무 공격적으로 치환하면 의미가 깨지므로, 자주 등장하는 BOJ 인명만 골라서 처리.
const KNOWN_NAMES: Array<[RegExp, (match: string, ...groups: string[]) => string]> = [
  [/(상근|창영|준규|정인|동주|민호|영수|영희|철수|구사과|준오)이?(가|는|을|를|와|에게|보다|라고)?/g,
   (_m, _name, particle) => `포켓몬마스터${particle ?? ""}`]
];

// ---- 한국어 조사 보정 ----
// 명사를 치환한 뒤 다음 조사가 받침과 안 맞는 경우(예: '마을와' → '마을과') 보정.
const NORMALIZED_WORDS = [
  "마을", "포켓몬마을", "포켓몬 학교", "포켓몬 길드",
  "트레이너", "수련생", "체육관 관장", "동료 트레이너",
  "배지카드", "포켓머니", "도구", "도감", "길"
];

function hasJongsung(ch: string): boolean | null {
  if (!ch) return null;
  const c = ch.charCodeAt(ch.length - 1);
  if (c < 0xAC00 || c > 0xD7A3) return null;
  return (c - 0xAC00) % 28 !== 0;
}

function fixParticles(s: string, words: string[]): string {
  for (const w of words) {
    const has = hasJongsung(w);
    if (has === null) continue;
    const wEsc = w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    // 받침 O → 이/은/을/과/으로, 받침 X → 가/는/를/와/로
    const pairs: Array<[string, string]> = has
      ? [["가", "이"], ["는", "은"], ["를", "을"], ["와", "과"], ["로", "으로"]]
      : [["이", "가"], ["은", "는"], ["을", "를"], ["과", "와"], ["으로", "로"]];
    for (const [from, to] of pairs) {
      // 단어 직후의 잘못된 조사 → 올바른 조사로. 다음 글자가 한글이면 합성어로 보고 건너뜀.
      const re = new RegExp(`(${wEsc})${from}(?![가-힣A-Za-z0-9_])`, "g");
      s = s.replace(re, `$1${to}`);
    }
  }
  return s;
}

// ---- 메인 ----
export type AdaptedText = {
  description: string;
  input: string;
  output: string;
  intro: string;
};

export function adaptForPokemon(
  problem: Problem,
  monster: MonsterMapEntry,
  text: { description: string; input: string; output: string }
): AdaptedText {
  const r = rng(`adapt:${problem.slug}:${monster.no}`);
  const trainer = pick(r, TRAINERS);
  const town    = pick(r, TOWNS);
  const motif   = motifFor(problem.categorySlug);

  function transform(s: string): string {
    if (!s) return s;
    let out = s;
    // 인명 치환 먼저
    for (const [re, rep] of KNOWN_NAMES) {
      out = out.replace(re, rep);
    }
    // 일반 명사 치환
    for (const [re, rep] of motif.replacements) {
      const r2 = typeof rep === "function" ? rep(monster) : rep;
      out = out.replace(re, r2);
    }
    // 한국어 조사 자동 보정 (받침 유무에 맞게 이/가, 은/는, 을/를, 과/와, 으로/로)
    out = fixParticles(out, NORMALIZED_WORDS);
    return out;
  }

  return {
    intro:       motif.intro(monster, trainer, town),
    description: transform(text.description),
    input:       transform(text.input),
    output:      transform(text.output)
  };
}
