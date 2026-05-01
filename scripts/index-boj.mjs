// 백준 솔루션 폴더(C:\Users\pcuser\Desktop\BOJ\baekjoon\solution)를 스캔해
// data/problems.json + data/categories.json 을 생성한다.
//
// 출력 스키마(엄격):
//   Category { slug, name_ko, name_en, type, problemCount }
//   Problem  { id, slug, categorySlug, sources: { lang, file, code }[],
//              link, authors[], hash, createdAt }
//
// 디자인 결정:
// - BOJ 폴더 위치는 환경변수 BOJ_ROOT 로 override 가능 (기본: ../BOJ/baekjoon)
// - 메타데이터는 솔루션 파일 헤더 주석에서 'Authored by' / 'Link' 만 안전 추출
// - 한글명은 lib/categoryMap.ts (런타임 import 가능)에서 join

import { readdir, readFile, writeFile, mkdir, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import { createHash } from "node:crypto";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname  = path.dirname(__filename);
const ROOT       = path.resolve(__dirname, "..");
const BOJ_ROOT   = process.env.BOJ_ROOT
  ? path.resolve(process.env.BOJ_ROOT)
  : path.resolve(ROOT, "..", "..", "BOJ", "baekjoon");
const SOLUTION_DIR = path.join(BOJ_ROOT, "solution");
const DATA_DIR     = path.join(ROOT, "data");

// 분류 → 한글명 + 포켓몬 타입 매핑
const CATEGORY_META = {
  brute_force:                 { ko: "완전탐색",     type: "fighting" },
  backtracking:                { ko: "백트래킹",     type: "ghost" },
  binary_search:               { ko: "이분탐색",     type: "ice" },
  data_structure:              { ko: "자료구조 I",   type: "rock" },
  data_structure2:             { ko: "자료구조 II",  type: "rock" },
  disjoint_set:                { ko: "분리집합",     type: "poison" },
  divide_and_conquer:          { ko: "분할정복",     type: "dark" },
  dynamic_programming_1:       { ko: "DP I",         type: "psychic" },
  dynamic_programming_2:       { ko: "DP II",        type: "psychic" },
  dynamic_programming_on_trees:{ ko: "트리 DP",      type: "psychic" },
  graph_traversal:             { ko: "그래프 탐색",  type: "flying" },
  greedy:                      { ko: "그리디",       type: "fire" },
  implementation:              { ko: "구현",         type: "bug" },
  math:                        { ko: "수학",         type: "steel" },
  minimum_spanning_tree:       { ko: "MST",          type: "fairy" },
  prefix_sum:                  { ko: "누적합",       type: "ground" },
  shortest_path:               { ko: "최단경로",     type: "electric" },
  simulation:                  { ko: "시뮬레이션",   type: "water" },
  string:                      { ko: "문자열",       type: "normal" },
  tree:                        { ko: "트리",         type: "grass" },
  trie:                        { ko: "트라이",       type: "grass" },
  two_pointer:                 { ko: "투 포인터",    type: "dragon" }
};

const LANG_BY_EXT = {
  ".py":   "python",
  ".cpp":  "cpp",
  ".cc":   "cpp",
  ".java": "java",
  ".js":   "javascript",
  ".ts":   "typescript",
  ".kt":   "kotlin",
  ".go":   "go",
  ".rs":   "rust",
  ".c":    "c"
};

const HEADER_AUTHOR = /Authored by\s*:\s*(.+)/i;
const HEADER_COAUTH = /Co-authored by\s*:\s*(.+)/i;
const HEADER_LINK   = /Link\s*:\s*(https?:\/\/\S+)/i;

function parseHeader(code) {
  const head = code.split(/\r?\n/).slice(0, 6).join("\n");
  const author = head.match(HEADER_AUTHOR)?.[1]?.trim();
  const co     = head.match(HEADER_COAUTH)?.[1]?.trim();
  const link   = head.match(HEADER_LINK)?.[1]?.trim();
  const authors = [];
  if (author && author !== "-") authors.push(author);
  if (co && co !== "-") authors.push(co);
  return { authors, link: link ?? null };
}

async function* walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) yield* walk(p);
    else yield p;
  }
}

async function main() {
  if (!existsSync(SOLUTION_DIR)) {
    console.error(`[index-boj] BOJ solution dir not found: ${SOLUTION_DIR}`);
    process.exit(1);
  }
  await mkdir(DATA_DIR, { recursive: true });

  const categoryDirs = (await readdir(SOLUTION_DIR, { withFileTypes: true }))
    .filter((d) => d.isDirectory())
    .map((d) => d.name);

  const categories = [];
  const problems = [];

  for (const slug of categoryDirs) {
    const meta = CATEGORY_META[slug] ?? { ko: slug, type: "normal" };
    const catDir = path.join(SOLUTION_DIR, slug);
    const problemDirs = (await readdir(catDir, { withFileTypes: true }))
      .filter((d) => d.isDirectory())
      .map((d) => d.name);

    let count = 0;
    for (const pid of problemDirs) {
      // BOJ 문제번호는 정수만 인정
      if (!/^\d+$/.test(pid)) continue;
      const pdir = path.join(catDir, pid);
      const sources = [];
      let header = { authors: [], link: null };

      for await (const file of walk(pdir)) {
        const ext = path.extname(file).toLowerCase();
        const lang = LANG_BY_EXT[ext];
        if (!lang) continue;
        const code = await readFile(file, "utf8");
        sources.push({ lang, file: path.relative(BOJ_ROOT, file).replaceAll("\\", "/"), code });
        const h = parseHeader(code);
        if (header.authors.length === 0) header.authors = h.authors;
        if (!header.link) header.link = h.link;
      }
      if (sources.length === 0) continue;

      const st = await stat(pdir);
      const hash = createHash("sha1").update(slug + ":" + pid).digest("hex").slice(0, 12);

      problems.push({
        id: pid,
        slug: `${slug}-${pid}`,
        categorySlug: slug,
        sources,
        link: header.link,
        authors: header.authors,
        hash,
        createdAt: st.birthtimeMs || st.mtimeMs
      });
      count++;
    }

    categories.push({
      slug,
      name_ko: meta.ko,
      name_en: slug,
      type: meta.type,
      problemCount: count
    });
  }

  problems.sort((a, b) => Number(a.id) - Number(b.id));
  categories.sort((a, b) => a.name_ko.localeCompare(b.name_ko, "ko"));

  await writeFile(path.join(DATA_DIR, "categories.json"), JSON.stringify(categories, null, 2), "utf8");
  await writeFile(path.join(DATA_DIR, "problems.json"),   JSON.stringify(problems, null, 2),   "utf8");

  console.log(`[index-boj] categories: ${categories.length}, problems: ${problems.length}`);
  console.log(`[index-boj] wrote ${path.relative(ROOT, DATA_DIR)}/{categories,problems}.json`);
}

main().catch((e) => { console.error(e); process.exit(1); });
