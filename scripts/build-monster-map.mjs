// 문제 ↔ 포켓몬 결정적 매핑 빌더 (v2 — solved.ac tier 기반).
//
// 우선순위:
//  1) data/problems-meta.json 의 level (1~30) 사용
//     - level >= 21 (Diamond+) : 환상 포켓몬 우선
//     - level 16~20 (Platinum) : 전설 포켓몬
//     - level 11~15 (Gold)     : 희귀
//     - level  6~10 (Silver)   : 고급
//     - level  1~5  (Bronze)   : 일반
//  2) 메타 없음/Unrated: 자릿수 fallback

import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT      = path.resolve(__dirname, "..");
const DATA_DIR  = path.join(ROOT, "data");

function rng(seedStr) {
  let h = 2166136261;
  for (let i = 0; i < seedStr.length; i++) {
    h ^= seedStr.charCodeAt(i);
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
function shuffleDet(arr, seedStr) {
  const r = rng(seedStr);
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(r() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function rarityOfProblem(level, id) {
  // 단순 임계점 기반 (percentile 매퍼가 따로 적용됨)
  if (level >= 21) return "mythical";
  if (level >= 14) return "legendary";
  if (level >= 9)  return "rare";
  if (level >= 4)  return "uncommon";
  if (level >= 1)  return "common";
  const d = String(id).length;
  if (d >= 5) return "rare";
  if (d === 4) return "uncommon";
  return "common";
}

// percentile 기반 등급 분포 강제 (시각적 다양성)
// 상위 5% mythical, 다음 15% legendary, 30% rare, 30% uncommon, 나머지 common
function buildPercentileRarities(enriched) {
  const ranked = [...enriched]
    .map(e => ({ slug: e.slug, score: e.level * 1000 + Number(e.id) }))
    .sort((a, b) => b.score - a.score);
  const N = ranked.length;
  const cuts = {
    mythical:  Math.floor(N * 0.05),
    legendary: Math.floor(N * 0.20),
    rare:      Math.floor(N * 0.50),
    uncommon:  Math.floor(N * 0.80)
  };
  const out = new Map();
  ranked.forEach((r, i) => {
    let rarity;
    if      (i < cuts.mythical)  rarity = "mythical";
    else if (i < cuts.legendary) rarity = "legendary";
    else if (i < cuts.rare)      rarity = "rare";
    else if (i < cuts.uncommon)  rarity = "uncommon";
    else                         rarity = "common";
    out.set(r.slug, rarity);
  });
  return out;
}

async function main() {
  await mkdir(DATA_DIR, { recursive: true });
  const problems = JSON.parse(await readFile(path.join(DATA_DIR, "problems.json"), "utf8"));
  const dex      = JSON.parse(await readFile(path.join(DATA_DIR, "pokedex.json"), "utf8"));
  const meta     = JSON.parse(await readFile(path.join(DATA_DIR, "problems-meta.json"), "utf8"));

  const enriched = problems.map(p => {
    const m = meta[p.id];
    const level = m?.level ?? 0;
    return { slug: p.slug, id: p.id, level };
  });
  const rarityBySlug = buildPercentileRarities(enriched);
  for (const e of enriched) e.rarity = rarityBySlug.get(e.slug) ?? rarityOfProblem(e.level, e.id);

  const pools = {
    mythical:  dex.filter(d => d.isMythical),
    legendary: dex.filter(d => d.isLegendary && !d.isMythical),
    rare:      dex.filter(d => !d.isLegendary && !d.isMythical && d.no >= 700),
    uncommon:  dex.filter(d => !d.isLegendary && !d.isMythical && d.no >= 300 && d.no < 700),
    common:    dex.filter(d => !d.isLegendary && !d.isMythical && d.no < 300)
  };
  for (const k of Object.keys(pools)) {
    pools[k] = shuffleDet(pools[k], `dongjun:${k}:v2`);
  }

  enriched.sort((a, b) => b.level - a.level || Number(a.id) - Number(b.id));

  const map = {};
  const cursors = { mythical:0, legendary:0, rare:0, uncommon:0, common:0 };

  const fallbackOrder = {
    mythical:  ["mythical","legendary","rare","uncommon","common"],
    legendary: ["legendary","mythical","rare","uncommon","common"],
    rare:      ["rare","uncommon","common"],
    uncommon:  ["uncommon","common"],
    common:    ["common","uncommon"]
  };

  for (const e of enriched) {
    let picked = null, finalRarity = e.rarity;
    for (const r of fallbackOrder[e.rarity]) {
      if (cursors[r] < pools[r].length) {
        picked = pools[r][cursors[r]++];
        finalRarity = r;
        break;
      }
    }
    if (!picked) throw new Error("All pools exhausted");

    let appliedRarity = finalRarity;
    if (picked.isMythical)       appliedRarity = "mythical";
    else if (picked.isLegendary) appliedRarity = "legendary";

    map[e.slug] = {
      no: picked.no,
      ko: picked.ko,
      en: picked.en,
      isLegendary: picked.isLegendary,
      isMythical:  picked.isMythical,
      generation:  picked.generation,
      types:       picked.types,
      rarity:      appliedRarity,
      level:       e.level
    };
  }

  await writeFile(path.join(DATA_DIR, "monster-map.json"), JSON.stringify(map), "utf8");

  const counts = { common:0, uncommon:0, rare:0, legendary:0, mythical:0 };
  for (const v of Object.values(map)) counts[v.rarity]++;
  console.log(`[monster-map] ${Object.keys(map).length} mappings`);
  console.log(`[monster-map] rarities:`, counts);
}

main().catch(e => { console.error(e); process.exit(1); });
