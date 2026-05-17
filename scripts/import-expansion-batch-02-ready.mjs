import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import https from "node:https";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");

const READY_IDS = ["15886", "14697", "2638", "1238", "2602"];
const BATCH_PATH = path.join(DATA_DIR, "problem-expansion-batch-02.json");
const OUT = path.join(DATA_DIR, "problems-extra.json");
const LANG_PRIORITY = ["python", "cpp"];

const LOCAL_SOURCE_BY_ID = {
  "14697": {
    lang: "python",
    file: "local/oracle/brute_force-14697.py",
    code: `import sys

a, b, c, n = map(int, sys.stdin.readline().split())
ok = 0
for x in range(n // a + 1):
    for y in range(n // b + 1):
        rest = n - a * x - b * y
        if rest >= 0 and rest % c == 0:
            ok = 1
print(ok)
`
  },
  "2602": {
    lang: "python",
    file: "local/oracle/dynamic_programming_2-2602.py",
    code: `import sys

target = sys.stdin.readline().strip()
devil = sys.stdin.readline().strip()
angel = sys.stdin.readline().strip()
bridges = [devil, angel]
n = len(target)
m = len(devil)

dp = [[[0] * m for _ in range(n)] for _ in range(2)]
for b in range(2):
    for i, ch in enumerate(bridges[b]):
        if ch == target[0]:
            dp[b][0][i] = 1

for k in range(1, n):
    for b in range(2):
        other = 1 - b
        running = 0
        for pos in range(m):
            running += dp[other][k - 1][pos - 1] if pos > 0 else 0
            if bridges[b][pos] == target[k]:
                dp[b][k][pos] = running

print(sum(dp[0][n - 1]) + sum(dp[1][n - 1]))
`
  }
};

function get(url) {
  return new Promise((resolve, reject) => {
    https
      .get(url, { headers: { "User-Agent": "DongJun-CodeDex" } }, (res) => {
        let body = "";
        res.setEncoding("utf8");
        res.on("data", (chunk) => {
          body += chunk;
        });
        res.on("end", () => {
          if (res.statusCode && res.statusCode >= 400) {
            reject(new Error(`GET ${url} failed: ${res.statusCode}`));
            return;
          }
          resolve(body);
        });
      })
      .on("error", reject);
  });
}

async function readJson(file, fallback) {
  try {
    return JSON.parse(await fs.readFile(file, "utf8"));
  } catch {
    return fallback;
  }
}

function stableHash(value) {
  return createHash("sha1").update(value).digest("hex").slice(0, 12);
}

function pickSourceFiles(candidate) {
  const supported = (candidate.externalSourceFiles ?? []).filter((file) => LANG_PRIORITY.includes(file.lang));
  supported.sort((a, b) => LANG_PRIORITY.indexOf(a.lang) - LANG_PRIORITY.indexOf(b.lang));
  return supported;
}

async function buildProblem(candidate) {
  const sources = [];
  if (LOCAL_SOURCE_BY_ID[candidate.id]) {
    sources.push(LOCAL_SOURCE_BY_ID[candidate.id]);
  }

  for (const file of pickSourceFiles(candidate)) {
    sources.push({
      lang: file.lang,
      file: file.htmlUrl,
      code: await get(file.downloadUrl)
    });
  }

  if (sources.length === 0) {
    throw new Error(`no supported source for ${candidate.slug}`);
  }

  return {
    id: candidate.id,
    slug: candidate.slug,
    categorySlug: candidate.primaryCategory,
    sources,
    link: `https://www.acmicpc.net/problem/${candidate.id}`,
    authors: ["tony9402"],
    hash: stableHash(`extra:${candidate.slug}`),
    createdAt: Date.now()
  };
}

async function main() {
  const [batch, existingExtra] = await Promise.all([
    readJson(BATCH_PATH, null),
    readJson(OUT, [])
  ]);
  if (!batch) throw new Error(`missing ${BATCH_PATH}`);

  const byId = new Map(batch.candidates.map((candidate) => [candidate.id, candidate]));
  const bySlug = new Map(existingExtra.map((problem) => [problem.slug, problem]));

  for (const id of READY_IDS) {
    const candidate = byId.get(id);
    if (!candidate) throw new Error(`candidate not found: ${id}`);
    const problem = await buildProblem(candidate);
    bySlug.set(problem.slug, problem);
    console.log(`[import-batch-02] imported ${problem.slug} (${problem.sources.map((s) => s.lang).join(", ")})`);
  }

  const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
  await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
  console.log(`[import-batch-02] wrote ${OUT}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
