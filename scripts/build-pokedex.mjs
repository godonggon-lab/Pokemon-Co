// 전국도감 데이터를 PokéAPI 에서 가져와 data/pokedex.json 생성.
// - 출력: [{ no, ko, en, isLegendary, isMythical, types: [string,...], generation }]
// - 캐시: 이미 data/pokedex.json 이 있고 --refresh 가 없으면 스킵
// - 동시성 제한 + 재시도, 실패 시 fallback (data/pokedex.fallback.json) 사용
//
// 사용:
//   node scripts/build-pokedex.mjs
//   node scripts/build-pokedex.mjs --refresh   # 강제 재생성
//   node scripts/build-pokedex.mjs --max=251   # 부분 빌드 (테스트)

import { mkdir, readFile, writeFile, access } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT      = path.resolve(__dirname, "..");
const DATA_DIR  = path.join(ROOT, "data");
const OUT       = path.join(DATA_DIR, "pokedex.json");
const FALLBACK  = path.join(DATA_DIR, "pokedex.fallback.json");

const args = new Set(process.argv.slice(2));
const REFRESH = args.has("--refresh");
const MAX_ARG = [...args].find((a) => a.startsWith("--max="));
const MAX_ID  = MAX_ARG ? parseInt(MAX_ARG.split("=")[1], 10) : 1025; // Gen 9 까지
const CONCURRENCY = 12;

const SPECIES_URL = (id) => `https://pokeapi.co/api/v2/pokemon-species/${id}/`;
const POKEMON_URL = (id) => `https://pokeapi.co/api/v2/pokemon/${id}/`;

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

function pickKo(names) {
  return names.find((n) => n.language?.name === "ko")?.name ?? null;
}

async function fetchOne(id) {
  const [sp, mon] = await Promise.all([
    fetchJson(SPECIES_URL(id)),
    fetchJson(POKEMON_URL(id)).catch(() => null)
  ]);
  return {
    no: id,
    ko: pickKo(sp.names) ?? sp.name,
    en: sp.name,
    isLegendary: !!sp.is_legendary,
    isMythical:  !!sp.is_mythical,
    generation:  parseGen(sp.generation?.name),
    types: mon?.types?.map((t) => t.type?.name).filter(Boolean) ?? []
  };
}

function parseGen(name) {
  if (!name) return 0;
  const m = name.match(/generation-([ivx]+)/);
  if (!m) return 0;
  const roman = m[1].toUpperCase();
  const map = { I:1, II:2, III:3, IV:4, V:5, VI:6, VII:7, VIII:8, IX:9 };
  return map[roman] ?? 0;
}

async function pool(items, fn, n) {
  const out = new Array(items.length);
  let i = 0;
  await Promise.all(Array.from({ length: n }, async () => {
    while (true) {
      const idx = i++;
      if (idx >= items.length) return;
      try { out[idx] = await fn(items[idx]); }
      catch (e) { console.warn(`  ! failed id=${items[idx]}: ${e.message}`); out[idx] = null; }
      if ((idx + 1) % 50 === 0) console.log(`  · ${idx + 1}/${items.length}`);
    }
  }));
  return out.filter(Boolean);
}

async function exists(p) { try { await access(p); return true; } catch { return false; } }

async function main() {
  await mkdir(DATA_DIR, { recursive: true });

  if (!REFRESH && (await exists(OUT))) {
    const cached = JSON.parse(await readFile(OUT, "utf8"));
    if (cached.length >= MAX_ID * 0.9) {
      console.log(`[pokedex] using cached ${OUT} (${cached.length} entries). Use --refresh to rebuild.`);
      return;
    }
  }

  console.log(`[pokedex] fetching 1..${MAX_ID} from PokéAPI (concurrency=${CONCURRENCY})...`);
  const ids = Array.from({ length: MAX_ID }, (_, i) => i + 1);

  let entries = [];
  try {
    entries = await pool(ids, fetchOne, CONCURRENCY);
  } catch (e) {
    console.error(`[pokedex] fetch failed: ${e.message}`);
    if (await exists(FALLBACK)) {
      console.log(`[pokedex] falling back to ${FALLBACK}`);
      entries = JSON.parse(await readFile(FALLBACK, "utf8"));
    } else {
      throw e;
    }
  }

  entries.sort((a, b) => a.no - b.no);
  await writeFile(OUT, JSON.stringify(entries, null, 0), "utf8");
  const leg = entries.filter((e) => e.isLegendary).length;
  const myth = entries.filter((e) => e.isMythical).length;
  console.log(`[pokedex] wrote ${entries.length} entries (legendary=${leg}, mythical=${myth})`);
}

main().catch((e) => { console.error(e); process.exit(1); });
