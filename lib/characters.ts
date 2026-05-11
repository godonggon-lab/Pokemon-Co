import monsterMapJson from "@/data/monster-map.json";
import type { Problem } from "./types";

export type Rarity = "bronze" | "silver" | "gold" | "platinum";

export type MonsterMapEntry = {
  no: number;
  ko: string;
  en: string;
  isLegendary: boolean;
  isMythical: boolean;
  generation: number;
  types: string[];
  rarity: Rarity;
  solvedTier?: Rarity;
  pokemonClass?: Rarity;
  reusedPokemon?: boolean;
  evolutionStage?: number;
  familyRoot?: string;
  level?: number;
  problemR?: number;
};

const MAP = monsterMapJson as unknown as Record<string, MonsterMapEntry>;

export function getMonsterEntry(slug: string): MonsterMapEntry | undefined {
  return MAP[slug];
}

function rng(seed: string) {
  let h = 2166136261;
  for (let i = 0; i < seed.length; i++) {
    h ^= seed.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  let s = h >>> 0;
  return () => {
    s |= 0;
    s = (s + 0x6D2B79F5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export type Monster = {
  problemSlug: string;
  dexNo: number;
  name: string;
  enName: string;
  rarity: Rarity;
  types: string[];
  generation: number;
  baseStats: { hp: number; atk: number; def: number; spd: number };
  spriteUrl: string;
  artworkUrl: string;
  fallbackEmoji: string;
};

const TYPE_EMOJI: Record<string, string> = {
  fire: "F",
  water: "W",
  grass: "G",
  electric: "E",
  ice: "I",
  fighting: "F",
  poison: "P",
  ground: "G",
  flying: "A",
  psychic: "P",
  bug: "B",
  rock: "R",
  ghost: "H",
  dragon: "D",
  dark: "D",
  steel: "S",
  fairy: "Y",
  normal: "N"
};

export function buildMonster(problem: Problem): Monster {
  const m = MAP[problem.slug];
  if (!m) {
    return {
      problemSlug: problem.slug,
      dexNo: 0,
      name: "???",
      enName: "?",
      rarity: "bronze",
      types: [],
      generation: 0,
      baseStats: { hp: 50, atk: 50, def: 50, spd: 50 },
      spriteUrl: "",
      artworkUrl: "",
      fallbackEmoji: "?"
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
      hp: 40 + Math.floor(r() * 60),
      atk: 30 + Math.floor(r() * 70),
      def: 30 + Math.floor(r() * 70),
      spd: 30 + Math.floor(r() * 70)
    },
    spriteUrl: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${m.no}.png`,
    artworkUrl: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${m.no}.png`,
    fallbackEmoji: m.types[0] ? (TYPE_EMOJI[m.types[0]] ?? "?") : "?"
  };
}

export const RARITY_LABEL: Record<Rarity, string> = {
  bronze: "브론즈",
  silver: "실버",
  gold: "골드",
  platinum: "플래티넘"
};

export const RARITY_RING: Record<Rarity, string> = {
  bronze: "ring-2 ring-orange-700",
  silver: "ring-2 ring-zinc-300",
  gold: "ring-2 ring-amber-400 shadow-[0_0_20px_rgba(245,158,11,0.45)]",
  platinum: "ring-2 ring-cyan-300 shadow-[0_0_28px_rgba(103,232,249,0.55)]"
};

export const RARITY_BG: Record<Rarity, string> = {
  bronze: "bg-orange-950/25",
  silver: "bg-zinc-700/25",
  gold: "bg-gradient-to-br from-amber-900/35 via-zinc-900 to-yellow-700/20",
  platinum: "bg-gradient-to-br from-cyan-900/35 via-zinc-900 to-indigo-700/20"
};

export const POKE_TYPE_BG: Record<string, string> = {
  fire: "bg-type-fire",
  water: "bg-type-water",
  grass: "bg-type-grass",
  electric: "bg-type-electric",
  ice: "bg-type-ice",
  fighting: "bg-type-fighting",
  poison: "bg-type-poison",
  ground: "bg-type-ground",
  flying: "bg-type-flying",
  psychic: "bg-type-psychic",
  bug: "bg-type-bug",
  rock: "bg-type-rock",
  ghost: "bg-type-ghost",
  dragon: "bg-type-dragon",
  dark: "bg-type-dark",
  steel: "bg-type-steel",
  fairy: "bg-type-fairy",
  normal: "bg-type-normal"
};

export const POKE_TYPE_KO: Record<string, string> = {
  fire: "불꽃",
  water: "물",
  grass: "풀",
  electric: "전기",
  ice: "얼음",
  fighting: "격투",
  poison: "독",
  ground: "땅",
  flying: "비행",
  psychic: "에스퍼",
  bug: "벌레",
  rock: "바위",
  ghost: "고스트",
  dragon: "드래곤",
  dark: "악",
  steel: "강철",
  fairy: "페어리",
  normal: "노말"
};
