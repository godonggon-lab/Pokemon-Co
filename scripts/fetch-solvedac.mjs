// solved.ac 에서 문제 메타데이터 수집.
// 출력: data/problems-meta.json
//   { [problemId]: { titleKo, level, levelName, tags[], acceptedCount, averageTries } }
//
// level 매핑:
//   1-5  Bronze  V..I    (브론즈)
//   6-10 Silver  V..I    (실버)
//   11-15 Gold V..I      (골드)
//   16-20 Platinum V..I  (플래티넘)
//   21-25 Diamond V..I   (다이아)
//   26-30 Ruby V..I      (루비)
//
// 사용:
//   node scripts/fetch-solvedac.mjs            # data/problems.json 의 모든 문제 수집
//   node scripts/fetch-solvedac.mjs --refresh  # 강제 재수집

import { readFile, writeFile, mkdir, access } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT      = path.resolve(__dirname, "..");
const DATA_DIR  = path.join(ROOT, "data");
const OUT       = path.join(DATA_DIR, "problems-meta.json");

const args = new Set(process.argv.slice(2));
const REFRESH = args.has("--refresh");
const CONCURRENCY = 3;

const TIER_NAMES = [
  "Unrated",
  "Bronze V","Bronze IV","Bronze III","Bronze II","Bronze I",
  "Silver V","Silver IV","Silver III","Silver II","Silver I",
  "Gold V","Gold IV","Gold III","Gold II","Gold I",
  "Platinum V","Platinum IV","Platinum III","Platinum II","Platinum I",
  "Diamond V","Diamond IV","Diamond III","Diamond II","Diamond I",
  "Ruby V","Ruby IV","Ruby III","Ruby II","Ruby I"
];

async function exists(p) { try { await access(p); return true; } catch { return false; } }

async function fetchJson(url, attempt = 0) {
  try {
    const r = await fetch(url, {
      headers: {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36",
        "accept": "application/json"
      }
    });
    if (r.status === 404) return null;
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    return await r.json();
  } catch (e) {
    if (attempt >= 3) throw e;
    await new Promise(res => setTimeout(res, 600 * (attempt + 1)));
    return fetchJson(url, attempt + 1);
  }
}

async function pool(items, fn, n) {
  const out = [];
  let idx = 0;
  await Promise.all(Array.from({ length: n }, async () => {
    while (true) {
      const i = idx++;
      if (i >= items.length) return;
      try {
        const v = await fn(items[i]);
        if (v) out.push(v);
      } catch (e) {
        console.warn(`  ! ${items[i]}: ${e.message}`);
      }
      if ((i + 1) % 25 === 0) console.log(`  · ${i + 1}/${items.length}`);
    }
  }));
  return out;
}

async function fetchOne(id) {
  const j = await fetchJson(`https://solved.ac/api/v3/problem/show?problemId=${id}`);
  if (!j) return null;
  const tags = (j.tags ?? []).map(t => ({
    key: t.key,
    name_ko: t.displayNames?.find(d => d.language === "ko")?.name ?? t.key
  }));
  return [String(id), {
    titleKo: j.titleKo,
    level: j.level,
    levelName: TIER_NAMES[j.level] ?? "Unrated",
    tags,
    acceptedCount: j.acceptedUserCount ?? 0,
    averageTries: j.averageTries ?? 0
  }];
}

async function main() {
  await mkdir(DATA_DIR, { recursive: true });
  let cache = {};
  if (!REFRESH && await exists(OUT)) {
    cache = JSON.parse(await readFile(OUT, "utf8"));
  }

  const problems = JSON.parse(await readFile(path.join(DATA_DIR, "problems.json"), "utf8"));
  const need = problems.map(p => p.id).filter(id => !cache[id]);
  console.log(`[solvedac] need=${need.length} cached=${Object.keys(cache).length} total=${problems.length}`);

  if (need.length === 0) {
    console.log(`[solvedac] up-to-date.`);
    return;
  }

  // 1차: bulk lookup (100개씩) — show 보다 안정적
  for (let i = 0; i < need.length; i += 100) {
    const chunk = need.slice(i, i + 100);
    try {
      const arr = await fetchJson(
        `https://solved.ac/api/v3/problem/lookup?problemIds=${chunk.join(",")}`
      );
      if (Array.isArray(arr)) {
        for (const j of arr) {
          const tags = (j.tags ?? []).map(t => ({
            key: t.key,
            name_ko: t.displayNames?.find(d => d.language === "ko")?.name ?? t.key
          }));
          cache[String(j.problemId)] = {
            titleKo: j.titleKo,
            level: j.level,
            levelName: TIER_NAMES[j.level] ?? "Unrated",
            tags,
            acceptedCount: j.acceptedUserCount ?? 0,
            averageTries: j.averageTries ?? 0
          };
        }
        console.log(`  · bulk ${i + chunk.length}/${need.length}`);
      }
    } catch (e) {
      console.warn(`  ! bulk failed at ${i}: ${e.message}`);
    }
    await new Promise(r => setTimeout(r, 800));
  }

  // 2차: 여전히 missing 인 항목만 single (희귀)
  const stillMissing = problems.map(p => p.id).filter(id => !cache[id]);
  if (stillMissing.length) {
    console.log(`[solvedac] single-fallback for ${stillMissing.length}`);
    const fetched = await pool(stillMissing, fetchOne, CONCURRENCY);
    for (const [id, meta] of fetched) cache[id] = meta;
  }

  await writeFile(OUT, JSON.stringify(cache, null, 0), "utf8");
  console.log(`[solvedac] wrote ${Object.keys(cache).length} entries`);
}

main().catch(e => { console.error(e); process.exit(1); });
