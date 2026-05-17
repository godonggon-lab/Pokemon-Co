import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import https from "node:https";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");

const FIRST_5_PATH = path.join(DATA_DIR, "problem-expansion-first-5.json");
const OUT = path.join(DATA_DIR, "problems-extra.json");

const LANG_PRIORITY = ["python", "cpp"];

const LOCAL_SOURCE_BY_ID = {
  "4949": {
    lang: "python",
    file: "local/oracle/data_structure-4949.py",
    code: `import sys

pairs = {")": "(", "]": "["}

def balanced(line):
    stack = []
    for ch in line:
        if ch in "([":
            stack.append(ch)
        elif ch in ")]":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

out = []
for line in sys.stdin.read().splitlines():
    if line == ".":
        break
    out.append("yes" if balanced(line) else "no")
print("\\n".join(out))
`
  }
};

function get(url) {
  return new Promise((resolve, reject) => {
    https
      .get(
        url,
        {
          headers: {
            "User-Agent": "DongJun-CodeDex"
          }
        },
        (res) => {
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
        }
      )
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
  const supported = candidate.sourceFiles.filter((file) => LANG_PRIORITY.includes(file.lang));
  supported.sort((a, b) => LANG_PRIORITY.indexOf(a.lang) - LANG_PRIORITY.indexOf(b.lang));
  return supported;
}

async function buildProblem(candidate) {
  const sourceFiles = pickSourceFiles(candidate);
  if (sourceFiles.length === 0) {
    throw new Error(`no supported source file: ${candidate.id}`);
  }

  const sources = [];
  if (LOCAL_SOURCE_BY_ID[candidate.id]) {
    sources.push(LOCAL_SOURCE_BY_ID[candidate.id]);
  }
  for (const file of sourceFiles) {
    sources.push({
      lang: file.lang,
      file: file.htmlUrl,
      code: await get(file.downloadUrl)
    });
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
  const [first5, existingExtra] = await Promise.all([
    readJson(FIRST_5_PATH, null),
    readJson(OUT, [])
  ]);
  if (!first5) throw new Error(`missing ${FIRST_5_PATH}`);

  const bySlug = new Map(existingExtra.map((problem) => [problem.slug, problem]));
  for (const candidate of first5.candidates) {
    const problem = await buildProblem(candidate);
    bySlug.set(problem.slug, problem);
    console.log(`[import-first-5] imported ${problem.slug} (${problem.sources.map((s) => s.lang).join(", ")})`);
  }

  const problems = [...bySlug.values()].sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));
  await fs.writeFile(OUT, JSON.stringify(problems, null, 2), "utf8");
  console.log(`[import-first-5] wrote ${OUT}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
