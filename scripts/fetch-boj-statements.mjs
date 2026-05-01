// BOJ 문제 본문 페처 — Wayback Machine 활용.
//
// 흐름:
//   1) CDX API 로 각 문제의 200 OK 스냅샷 후보 5개 수집 (최신순)
//   2) 각 후보를 /web/<ts>id_/ 로 시도 → BOJ 정상 응답이면 채택
//   3) HTML 에서 problem_description / problem_input / problem_output / sample-* 추출
//   4) data/problems-statements.json 누적 캐시
//
// 재시도/리쥼:
//   - 이미 캐시된 문제는 스킵 (--force 로 강제)
//   - 실패한 문제는 별도 keys 에 기록해 다음 실행에서 재시도

import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const DATA = path.join(ROOT, "data");

const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36";
const FORCE = process.argv.includes("--force");
const ONLY  = process.argv.find(a => a.startsWith("--only="))?.slice(7); // ex: --only=1000,2798
const LIMIT = Number(process.argv.find(a => a.startsWith("--limit="))?.slice(8) || 0);
const CONCURRENCY = Number(process.argv.find(a => a.startsWith("--concurrency="))?.slice(14) || 1);
const POLITE_MS   = Number(process.argv.find(a => a.startsWith("--delay="))?.slice(8) || 1500);

// ---------- HTML 파싱 ----------
function decodeEntities(s) {
  return s
    .replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'")
    .replace(/&amp;/g, "&").replace(/&nbsp;/g, " ")
    // 수학 엔티티
    .replace(/&le;/g, "≤").replace(/&ge;/g, "≥")
    .replace(/&ne;/g, "≠").replace(/&times;/g, "×")
    .replace(/&divide;/g, "÷").replace(/&middot;/g, "·")
    .replace(/&minus;/g, "−").replace(/&plusmn;/g, "±")
    .replace(/&lfloor;/g, "⌊").replace(/&rfloor;/g, "⌋")
    .replace(/&lceil;/g, "⌈").replace(/&rceil;/g, "⌉")
    .replace(/&infin;/g, "∞").replace(/&cup;/g, "∪")
    .replace(/&cap;/g, "∩").replace(/&sub;/g, "⊂")
    // 화살표
    .replace(/&larr;/g, "←").replace(/&rarr;/g, "→")
    .replace(/&uarr;/g, "↑").replace(/&darr;/g, "↓")
    .replace(/&harr;/g, "↔").replace(/&lArr;/g, "⇐")
    .replace(/&rArr;/g, "⇒").replace(/&hArr;/g, "⇔")
    // 그리스 문자
    .replace(/&alpha;/g, "α").replace(/&beta;/g, "β")
    .replace(/&gamma;/g, "γ").replace(/&delta;/g, "δ")
    .replace(/&epsilon;/g, "ε").replace(/&lambda;/g, "λ")
    .replace(/&mu;/g, "μ").replace(/&pi;/g, "π")
    .replace(/&sigma;/g, "σ").replace(/&theta;/g, "θ")
    // 기타
    .replace(/&hellip;/g, "…").replace(/&mdash;/g, "—")
    .replace(/&ndash;/g, "–")
    // 인용 부호
    .replace(/&lsquo;/g, "‘").replace(/&rsquo;/g, "’")
    .replace(/&ldquo;/g, "“").replace(/&rdquo;/g, "”")
    .replace(/&lsaquo;/g, "‹").replace(/&rsaquo;/g, "›")
    // 기타 자주 쓰이는 것
    .replace(/&deg;/g, "°").replace(/&micro;/g, "μ")
    .replace(/&copy;/g, "©").replace(/&reg;/g, "®")
    // 숫자 참조
    .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(Number(n)))
    .replace(/&#x([0-9a-fA-F]+);/g, (_, h) => String.fromCharCode(parseInt(h, 16)));
}

// 이미지 src를 절대 URL + Wayback 이미지 프록시(im_)로 재작성.
// BOJ 본 사이트는 닫혔으므로 wayback 경유가 유일한 표시 경로.
function rewriteImgSrc(src, ts) {
  if (!src) return "";
  let abs = src.trim();
  // wayback 자체 경로면 원본 추출 시도
  const wbm = abs.match(/web\.archive\.org\/web\/\d+(?:[a-z_]+)?\/(https?:\/\/.+)$/);
  if (wbm) abs = wbm[1];
  if (abs.startsWith("//")) abs = "https:" + abs;
  else if (abs.startsWith("/")) abs = "https://www.acmicpc.net" + abs;
  else if (!/^https?:\/\//i.test(abs)) return ""; // data: 등 스킵
  return `https://web.archive.org/web/${ts}im_/${abs}`;
}

function stripTags(html, ts) {
  return decodeEntities(
    html
      // <img>를 마크다운 형태로 보존 (alt 옵션)
      .replace(/<img\b[^>]*>/gi, (tag) => {
        const sm = tag.match(/\bsrc=["']([^"']+)["']/i);
        if (!sm) return "";
        const url = rewriteImgSrc(sm[1], ts);
        if (!url) return "";
        const am = tag.match(/\balt=["']([^"']*)["']/i);
        return `\n\n![${am ? am[1] : ""}](${url})\n\n`;
      })
      .replace(/<br\s*\/?>/gi, "\n")
      .replace(/<\/p>/gi, "\n\n")
      .replace(/<li>/gi, "• ")
      .replace(/<\/li>/gi, "\n")
      .replace(/<[^>]+>/g, "")
  ).replace(/\n{3,}/g, "\n\n").trim();
}

function extractSection(html, id, ts) {
  // <... id="problem_description" ...> ... </section> 또는 </div>
  const re = new RegExp(`id="${id}"[^>]*>([\\s\\S]*?)(?=<section|<div\\s+id="problem_|<div\\s+class="problem-section|<h[12])`, "i");
  const m = html.match(re);
  if (!m) return "";
  return stripTags(m[1], ts);
}

function extractSamples(html) {
  const samples = [];
  const re = /id="sample-input-(\d+)"[^>]*>([\s\S]*?)<\/pre>[\s\S]*?id="sample-output-\1"[^>]*>([\s\S]*?)<\/pre>/g;
  let m;
  while ((m = re.exec(html)) !== null) {
    samples.push({
      idx: Number(m[1]),
      in:  decodeEntities(m[2]).replace(/^\s+|\s+$/g, ""),
      out: decodeEntities(m[3]).replace(/^\s+|\s+$/g, "")
    });
  }
  samples.sort((a, b) => a.idx - b.idx);
  return samples;
}

function extractLimits(html) {
  // 시간/메모리는 problem-info table 에 있음
  const out = { timeLimitMs: null, memoryLimitMb: null };
  const tlMatch = html.match(/<th[^>]*>\s*시간 제한[\s\S]*?<td[^>]*>([\s\S]*?)<\/td>/);
  if (tlMatch) {
    const sec = Number((stripTags(tlMatch[1], "").match(/[\d.]+/) || [])[0]);
    if (Number.isFinite(sec)) out.timeLimitMs = Math.round(sec * 1000);
  }
  const mlMatch = html.match(/<th[^>]*>\s*메모리 제한[\s\S]*?<td[^>]*>([\s\S]*?)<\/td>/);
  if (mlMatch) {
    const mb = Number((stripTags(mlMatch[1], "").match(/[\d.]+/) || [])[0]);
    if (Number.isFinite(mb)) out.memoryLimitMb = Math.round(mb);
  }
  return out;
}

function parseBojHtml(html, ts) {
  const titleMatch = html.match(/<title>(\d+)번:\s*([^<]+?)<\/title>/);
  if (!titleMatch) return null;
  const description = extractSection(html, "problem_description", ts);
  const input       = extractSection(html, "problem_input", ts);
  const output      = extractSection(html, "problem_output", ts);
  const limit       = extractSection(html, "problem_limit", ts);
  const hint        = extractSection(html, "problem_hint", ts);
  const samples     = extractSamples(html);
  const limits      = extractLimits(html);
  // 최소한 description 또는 input/output 중 하나는 있어야 함
  if (!description && !input && !output) return null;
  return {
    title: titleMatch[2].trim(),
    description, input, output, limit, hint,
    samples, limits
  };
}

// ---------- Wayback ----------
async function wbSnapshots(problemId) {
  // 모든 시기 스냅샷, 최대 30개. 최신부터 시도하기 위해 timestamp desc.
  const url = `https://web.archive.org/cdx/search/cdx?url=acmicpc.net/problem/${problemId}` +
              `&output=json&filter=statuscode:200&limit=30&fl=timestamp`;
  const r = await fetch(url, { headers: { "User-Agent": UA } });
  if (!r.ok) return [];
  const arr = await r.json();
  if (!Array.isArray(arr) || arr.length < 2) return [];
  return arr.slice(1)
    .map(row => row[0])
    .filter(ts => /^\d{14}$/.test(ts))
    .sort((a, b) => b.localeCompare(a)); // 최신 우선
}

async function fetchSnapshot(problemId, ts) {
  const url = `https://web.archive.org/web/${ts}id_/https://www.acmicpc.net/problem/${problemId}`;
  const r = await fetch(url, { headers: { "User-Agent": UA } });
  if (r.status === 429 || r.status === 503) {
    // Wayback rate limit — 웨이틸 다음 보보 되도록 신호한다
    await sleep(8000);
    return null;
  }
  if (!r.ok) return null;
  const html = await r.text();
  if (/<title>40[34]/.test(html)) return null;
  if (!html.includes("problem_description")) return null;
  return html;
}

async function fetchProblem(problemId) {
  const tsList = await wbSnapshots(problemId);
  for (const ts of tsList) {
    try {
      const html = await fetchSnapshot(problemId, ts);
      if (!html) continue;
      const parsed = parseBojHtml(html, ts);
      if (parsed) return { ...parsed, snapshotTs: ts };
    } catch { /* try next */ }
    await sleep(POLITE_MS);
  }
  return null;
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

// ---------- main ----------
async function main() {
  await mkdir(DATA, { recursive: true });
  const problems = JSON.parse(await readFile(path.join(DATA, "problems.json"), "utf8"));

  const cachePath = path.join(DATA, "problems-statements.json");
  let cache = {};
  try { cache = JSON.parse(await readFile(cachePath, "utf8")); } catch {}

  let targets = problems;
  if (ONLY) {
    const set = new Set(ONLY.split(",").map(s => s.trim()));
    targets = problems.filter(p => set.has(p.id));
  } else if (!FORCE) {
    targets = problems.filter(p => !cache[p.id] || cache[p.id]._failed);
  }
  if (LIMIT) targets = targets.slice(0, LIMIT);

  console.log(`[boj-fetch] targets: ${targets.length} / total ${problems.length}`);

  let okCount = 0, failCount = 0, doneCount = 0;
  const queue = [...targets];

  async function worker(id) {
    while (queue.length) {
      const p = queue.shift();
      if (!p) break;
      try {
        const got = await fetchProblem(p.id);
        if (got) {
          cache[p.id] = got;
          okCount++;
          console.log(`  [w${id}] ok  ${p.id} "${got.title}" (snap=${got.snapshotTs}, samples=${got.samples.length})`);
        } else {
          cache[p.id] = { _failed: true, ts: Date.now() };
          failCount++;
          console.log(`  [w${id}] FAIL ${p.id}`);
        }
      } catch (e) {
        cache[p.id] = { _failed: true, error: String(e?.message ?? e), ts: Date.now() };
        failCount++;
        console.log(`  [w${id}] ERR  ${p.id} ${e?.message ?? e}`);
      }
      doneCount++;
      // 매 10개마다 부분 저장
      if (doneCount % 10 === 0) {
        await writeFile(cachePath, JSON.stringify(cache), "utf8");
      }
      await sleep(POLITE_MS);
    }
  }
  await Promise.all(Array.from({ length: CONCURRENCY }, (_, i) => worker(i + 1)));
  await writeFile(cachePath, JSON.stringify(cache), "utf8");

  const totalOk = Object.values(cache).filter(v => !v._failed).length;
  console.log(`\n[boj-fetch] this run: ok=${okCount} fail=${failCount}`);
  console.log(`[boj-fetch] total cached: ${totalOk}/${problems.length}`);
}

main().catch(e => { console.error(e); process.exit(1); });
