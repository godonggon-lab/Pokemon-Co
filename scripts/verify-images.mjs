// problems-statements.json 안의 모든 이미지 URL을 스캔하여
//  (1) 형식이 wayback im_ 프록시인지
//  (2) HEAD 요청으로 실제 200 응답이 오는지
// 검사한 뒤 리포트를 출력한다.
//
// 사용:
//   node scripts/verify-images.mjs [--check-network]
//   --check-network 가 없으면 형식 검사만 (오프라인).

import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const JSON_PATH = path.resolve(__dirname, "..", "data", "problems-statements.json");
const NET = process.argv.includes("--check-network");
const TIMEOUT_MS = 8000;
const CONCURRENCY = 8;

const stmts = JSON.parse(await readFile(JSON_PATH, "utf-8"));

const re = /!\[([^\]]*)\]\(([^)]+)\)/g;
const records = [];

for (const [pid, s] of Object.entries(stmts)) {
  if (!s || s._failed) continue;
  const fields = ["description", "input", "output", "limit", "hint"];
  let blob = "";
  for (const f of fields) blob += "\n" + (s[f] ?? "");
  let m;
  while ((m = re.exec(blob)) !== null) {
    records.push({ pid, title: s.title, alt: m[1], url: m[2] });
  }
}

console.log(`총 문제 수: ${Object.keys(stmts).length}`);
console.log(`이미지 포함 문제 수: ${new Set(records.map((r) => r.pid)).size}`);
console.log(`총 이미지 수: ${records.length}\n`);

// 형식 검증
const WAYBACK_RE = /^https:\/\/web\.archive\.org\/web\/\d{14}im_\//;
const malformed = records.filter((r) => !WAYBACK_RE.test(r.url));
console.log(`[형식] wayback im_ 프록시 형식이 아닌 이미지: ${malformed.length}`);
for (const r of malformed.slice(0, 10)) {
  console.log(`   - ${r.pid}: ${r.url}`);
}
if (malformed.length > 10) console.log(`   ... 외 ${malformed.length - 10}개`);

if (!NET) {
  console.log("\n(네트워크 검사 생략. --check-network 로 실제 응답 확인 가능)");
  process.exit(0);
}

// 네트워크 검사 (HEAD 요청)
console.log(`\n[네트워크] ${records.length}개 이미지 응답 확인 중...`);

async function head(url) {
  const ctrl = new AbortController();
  const tid = setTimeout(() => ctrl.abort(), TIMEOUT_MS);
  try {
    const r = await fetch(url, { method: "HEAD", redirect: "follow", signal: ctrl.signal });
    return r.status;
  } catch (e) {
    return `ERR:${e.name}`;
  } finally {
    clearTimeout(tid);
  }
}

const results = new Array(records.length);
let cursor = 0, done = 0;
async function worker() {
  while (true) {
    const i = cursor++;
    if (i >= records.length) return;
    results[i] = await head(records[i].url);
    done++;
    if (done % 20 === 0) process.stdout.write(`  ${done}/${records.length}\r`);
  }
}
await Promise.all(Array.from({ length: CONCURRENCY }, worker));

const bad = records.map((r, i) => ({ ...r, status: results[i] }))
  .filter((r) => !(typeof r.status === "number" && r.status >= 200 && r.status < 400));
console.log(`\n[네트워크] 실패/비-2xx 이미지: ${bad.length} / ${records.length}`);

const byPid = {};
for (const r of bad) (byPid[r.pid] ??= []).push(r);
for (const [pid, arr] of Object.entries(byPid).slice(0, 20)) {
  console.log(`   - ${pid} (${arr[0].title}): ${arr.length}건  예) ${arr[0].status}  ${arr[0].url.slice(0,100)}`);
}
