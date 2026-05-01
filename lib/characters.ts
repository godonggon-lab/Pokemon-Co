// 문제 ↔ 실제 포켓몬 매핑.
// 데이터: data/monster-map.json (build-monster-map.mjs 가 빌드타임 생성)
//        data/pokedex.json     (build-pokedex.mjs 가 PokéAPI 에서 수집)
//
// 기존 합성 캐릭터(emoji + 자작이름)를 실제 도감(전국도감) 으로 대체.

import type { Problem } from "./types";
import monsterMapJson from "@/data/monster-map.json";

export type Rarity = "common" | "uncommon" | "rare" | "legendary" | "mythical";

export type MonsterMapEntry = {
  no: number;
  ko: string;
  en: string;
  isLegendary: boolean;
  isMythical: boolean;
  generation: number;
  types: string[];
  rarity: Rarity;
  level?: number;
  problemR?: number;
};

const MAP = monsterMapJson as unknown as Record<string, MonsterMapEntry>;

export function getMonsterEntry(slug: string): MonsterMapEntry | undefined {
  return MAP[slug];
}

// 결정적 PRNG — 같은 문제 = 같은 스탯
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

export type Monster = {
  problemSlug: string;
  dexNo: number;            // 전국도감 번호 (실제)
  name: string;             // 한국어 정식 이름
  enName: string;
  rarity: Rarity;
  types: string[];
  generation: number;
  baseStats: { hp: number; atk: number; def: number; spd: number };
  spriteUrl: string;        // 일반 스프라이트
  artworkUrl: string;       // 공식 일러스트 (고해상)
  fallbackEmoji: string;    // 이미지 로드 실패 시 백업
};

const TYPE_EMOJI: Record<string, string> = {
  fire:"🔥", water:"💧", grass:"🌿", electric:"⚡", ice:"❄️",
  fighting:"🥊", poison:"☠️", ground:"🏜️", flying:"🪽", psychic:"🔮",
  bug:"🐛", rock:"🪨", ghost:"👻", dragon:"🐉", dark:"🌑",
  steel:"⚙️", fairy:"🧚", normal:"🐾"
};

export function buildMonster(problem: Problem): Monster {
  const m = MAP[problem.slug];
  if (!m) {
    return {
      problemSlug: problem.slug,
      dexNo: 0, name: "???", enName: "?", rarity: "common", types: [],
      generation: 0,
      baseStats: { hp: 50, atk: 50, def: 50, spd: 50 },
      spriteUrl: "", artworkUrl: "", fallbackEmoji: "❔"
    };
  }
  const r = rng(`${problem.hash}:${m.no}`);
  return {
    problemSlug: problem.slug,
    dexNo: m.no,
    name: m.ko,
    enName: m.en,
    rarity: m.rarity,
    types: m.types,
    generation: m.generation,
    baseStats: {
      hp:  40 + Math.floor(r() * 60),
      atk: 30 + Math.floor(r() * 70),
      def: 30 + Math.floor(r() * 70),
      spd: 30 + Math.floor(r() * 70)
    },
    spriteUrl:  `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${m.no}.png`,
    artworkUrl: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${m.no}.png`,
    fallbackEmoji: m.types[0] ? (TYPE_EMOJI[m.types[0]] ?? "❔") : "❔"
  };
}

export const RARITY_LABEL: Record<Rarity, string> = {
  common: "일반", uncommon: "고급", rare: "희귀", legendary: "전설", mythical: "환상"
};

export const RARITY_RING: Record<Rarity, string> = {
  common:    "ring-2 ring-zinc-400",
  uncommon:  "ring-2 ring-emerald-400",
  rare:      "ring-2 ring-sky-400",
  legendary: "ring-2 ring-amber-400 shadow-[0_0_24px_rgba(245,158,11,0.55)]",
  mythical:  "ring-2 ring-fuchsia-400 shadow-[0_0_28px_rgba(232,121,249,0.6)]"
};

export const RARITY_BG: Record<Rarity, string> = {
  common:    "bg-zinc-700/30",
  uncommon:  "bg-emerald-900/20",
  rare:      "bg-sky-900/25",
  legendary: "bg-gradient-to-br from-amber-900/40 via-zinc-900 to-amber-700/20",
  mythical:  "bg-gradient-to-br from-fuchsia-900/40 via-zinc-900 to-purple-700/20"
};

// 포켓몬 18타입 → tailwind colors.type.* 색상 키
export const POKE_TYPE_BG: Record<string, string> = {
  fire:"bg-type-fire", water:"bg-type-water", grass:"bg-type-grass",
  electric:"bg-type-electric", ice:"bg-type-ice", fighting:"bg-type-fighting",
  poison:"bg-type-poison", ground:"bg-type-ground", flying:"bg-type-flying",
  psychic:"bg-type-psychic", bug:"bg-type-bug", rock:"bg-type-rock",
  ghost:"bg-type-ghost", dragon:"bg-type-dragon", dark:"bg-type-dark",
  steel:"bg-type-steel", fairy:"bg-type-fairy", normal:"bg-type-normal"
};

export const POKE_TYPE_KO: Record<string, string> = {
  fire:"불꽃", water:"물", grass:"풀", electric:"전기", ice:"얼음",
  fighting:"격투", poison:"독", ground:"땅", flying:"비행", psychic:"에스퍼",
  bug:"벌레", rock:"바위", ghost:"고스트", dragon:"드래곤", dark:"악",
  steel:"강철", fairy:"페어리", normal:"노말"
};
