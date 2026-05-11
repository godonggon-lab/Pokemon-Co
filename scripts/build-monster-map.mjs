// Build deterministic problem-to-Pokemon mapping.
//
// solved.ac level is collapsed into four product-facing classes:
// - Bronze   1..5   -> base / unevolved Pokemon
// - Silver   6..10  -> first evolution
// - Gold     11..15 -> second evolution
// - Platinum 16+    -> legendary or mythical Pokemon
//
// Problem order and Pokemon order are both deterministic. Within each class,
// problems are sorted by BOJ number and Pokemon are assigned by National Dex no.

import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");

function solvedTier(level) {
  if (level >= 16) return "platinum";
  if (level >= 11) return "gold";
  if (level >= 6) return "silver";
  return "bronze";
}

function fallbackLevel(id) {
  const n = Number(id);
  if (!Number.isFinite(n)) return 1;
  if (n >= 20000) return 11;
  if (n >= 10000) return 6;
  return 1;
}

function nextFromPool(pools, cursors, tier) {
  const pool = pools[tier];
  if (!pool.length) throw new Error(`Pokemon pool is empty: ${tier}`);
  const index = cursors[tier]++;
  return {
    pokemon: pool[index % pool.length],
    sourceTier: tier,
    reused: index >= pool.length
  };
}

async function main() {
  await mkdir(DATA_DIR, { recursive: true });
  const problems = JSON.parse(await readFile(path.join(DATA_DIR, "problems.json"), "utf8"));
  const taxonomy = JSON.parse(await readFile(path.join(DATA_DIR, "pokemon-taxonomy.json"), "utf8"));
  const meta = JSON.parse(await readFile(path.join(DATA_DIR, "problems-meta.json"), "utf8"));

  const enriched = problems.map((p) => {
    const level = meta[p.id]?.level ?? fallbackLevel(p.id);
    return {
      slug: p.slug,
      id: Number(p.id),
      level,
      solvedTier: solvedTier(level)
    };
  });

  const pools = {
    bronze: taxonomy.filter((p) => p.evolutionClass === "bronze"),
    silver: taxonomy.filter((p) => p.evolutionClass === "silver"),
    gold: taxonomy.filter((p) => p.evolutionClass === "gold"),
    platinum: taxonomy.filter((p) => p.evolutionClass === "platinum")
  };
  for (const key of Object.keys(pools)) {
    pools[key].sort((a, b) => a.no - b.no);
  }

  const map = {};
  const cursors = { bronze: 0, silver: 0, gold: 0, platinum: 0 };

  for (const tier of ["bronze", "silver", "gold", "platinum"]) {
    const bucket = enriched
      .filter((p) => p.solvedTier === tier)
      .sort((a, b) => a.id - b.id || a.slug.localeCompare(b.slug));

    for (const problem of bucket) {
      const { pokemon, sourceTier, reused } = nextFromPool(pools, cursors, tier);
      map[problem.slug] = {
        no: pokemon.no,
        ko: pokemon.ko,
        en: pokemon.en,
        isLegendary: pokemon.isLegendary,
        isMythical: pokemon.isMythical,
        generation: pokemon.generation,
        types: pokemon.types,
        rarity: tier,
        solvedTier: tier,
        pokemonClass: sourceTier,
        reusedPokemon: reused,
        evolutionStage: pokemon.evolutionStage,
        familyRoot: pokemon.familyRoot,
        level: problem.level
      };
    }
  }

  await writeFile(path.join(DATA_DIR, "monster-map.json"), JSON.stringify(map, null, 0), "utf8");

  const tierCounts = {};
  const pokemonCounts = {};
  for (const v of Object.values(map)) {
    tierCounts[v.solvedTier] = (tierCounts[v.solvedTier] ?? 0) + 1;
    pokemonCounts[v.pokemonClass] = (pokemonCounts[v.pokemonClass] ?? 0) + 1;
  }
  console.log(`[monster-map] ${Object.keys(map).length} mappings`);
  console.log("[monster-map] solved tiers:", tierCounts);
  console.log("[monster-map] pokemon classes:", pokemonCounts);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
