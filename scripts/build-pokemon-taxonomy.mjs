// Build Pokemon taxonomy used by problem-to-monster mapping.
//
// Output: data/pokemon-taxonomy.json
// - bronze: normal Pokemon with evolutionStage 0
// - silver: normal Pokemon with evolutionStage 1
// - gold: normal Pokemon with evolutionStage >= 2
// - platinum: legendary or mythical Pokemon
//
// The script is cached by default so normal builds do not depend on the network.
// Use --refresh to rebuild from PokeAPI evolution-chain data.

import { access, mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const POKEDEX = path.join(DATA_DIR, "pokedex.json");
const OUT = path.join(DATA_DIR, "pokemon-taxonomy.json");
const args = new Set(process.argv.slice(2));
const REFRESH = args.has("--refresh");
const CONCURRENCY = 12;

const SPECIES_URL = (id) => `https://pokeapi.co/api/v2/pokemon-species/${id}/`;

async function exists(p) {
  try {
    await access(p);
    return true;
  } catch {
    return false;
  }
}

async function fetchJson(url, attempt = 0) {
  try {
    const r = await fetch(url, { headers: { "user-agent": "DongJun-CodeDex-Builder/0.1" } });
    if (!r.ok) throw new Error(`HTTP ${r.status} ${url}`);
    return await r.json();
  } catch (e) {
    if (attempt >= 3) throw e;
    await new Promise((res) => setTimeout(res, 400 * (attempt + 1)));
    return fetchJson(url, attempt + 1);
  }
}

async function pool(items, fn, n) {
  const out = new Array(items.length);
  let i = 0;
  await Promise.all(Array.from({ length: n }, async () => {
    while (true) {
      const idx = i++;
      if (idx >= items.length) return;
      out[idx] = await fn(items[idx], idx);
      if ((idx + 1) % 100 === 0) console.log(`  - species ${idx + 1}/${items.length}`);
    }
  }));
  return out;
}

function walkChain(node, stage, rootName, stageByName, rootByName) {
  if (!node?.species?.name) return;
  stageByName.set(node.species.name, Math.min(stage, 2));
  rootByName.set(node.species.name, rootName);
  for (const next of node.evolves_to ?? []) {
    walkChain(next, stage + 1, rootName, stageByName, rootByName);
  }
}

function classOf(entry, stage) {
  if (entry.isLegendary || entry.isMythical) return "platinum";
  if (stage >= 2) return "gold";
  if (stage === 1) return "silver";
  return "bronze";
}

async function main() {
  await mkdir(DATA_DIR, { recursive: true });
  if (!REFRESH && await exists(OUT)) {
    const cached = JSON.parse(await readFile(OUT, "utf8"));
    console.log(`[pokemon-taxonomy] using cached ${OUT} (${cached.length} entries). Use --refresh to rebuild.`);
    return;
  }

  const pokedex = JSON.parse(await readFile(POKEDEX, "utf8"));
  console.log(`[pokemon-taxonomy] fetching species data for ${pokedex.length} Pokemon...`);
  const species = await pool(pokedex, (p) => fetchJson(SPECIES_URL(p.no)), CONCURRENCY);

  const chainUrls = [...new Set(species.map((s) => s.evolution_chain?.url).filter(Boolean))];
  console.log(`[pokemon-taxonomy] fetching ${chainUrls.length} evolution chains...`);
  const chains = await pool(chainUrls, (url) => fetchJson(url), CONCURRENCY);

  const stageByName = new Map();
  const rootByName = new Map();
  for (const chain of chains) {
    const rootName = chain?.chain?.species?.name;
    if (rootName) walkChain(chain.chain, 0, rootName, stageByName, rootByName);
  }

  const taxonomy = pokedex
    .map((p) => {
      const stage = stageByName.get(p.en) ?? 0;
      const evolutionClass = classOf(p, stage);
      return {
        ...p,
        evolutionStage: stage,
        evolutionClass,
        familyRoot: rootByName.get(p.en) ?? p.en
      };
    })
    .sort((a, b) => a.no - b.no);

  await writeFile(OUT, JSON.stringify(taxonomy, null, 0), "utf8");
  const counts = taxonomy.reduce((acc, p) => {
    acc[p.evolutionClass] = (acc[p.evolutionClass] ?? 0) + 1;
    return acc;
  }, {});
  console.log(`[pokemon-taxonomy] wrote ${taxonomy.length} entries`);
  console.log("[pokemon-taxonomy] classes:", counts);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
