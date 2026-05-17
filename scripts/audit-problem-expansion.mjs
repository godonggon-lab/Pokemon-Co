import fs from "node:fs/promises";
import https from "node:https";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const DOCS_DIR = path.join(ROOT, "docs");

const OWNER = process.env.BAEKJOON_REPO_OWNER ?? "godonggon-lab";
const REPO = process.env.BAEKJOON_REPO_NAME ?? "baekjoon";
const REF = process.env.BAEKJOON_REPO_REF ?? "main";
const TARGET_PROBLEM_COUNT = Number(process.env.TARGET_PROBLEM_COUNT ?? 1025);

const TREE_URL = `https://api.github.com/repos/${OWNER}/${REPO}/git/trees/${REF}?recursive=1`;
const RAW_BASE = `https://raw.githubusercontent.com/${OWNER}/${REPO}/${REF}`;

function get(url) {
  return new Promise((resolve, reject) => {
    https
      .get(
        url,
        {
          headers: {
            "User-Agent": "DongJun-CodeDex",
            Accept: "application/vnd.github+json"
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
              reject(new Error(`GET ${url} failed: ${res.statusCode} ${body.slice(0, 200)}`));
              return;
            }
            resolve(body);
          });
        }
      )
      .on("error", reject);
  });
}

function normalizeUrl(value) {
  const trimmed = (value ?? "").trim();
  return trimmed.startsWith("http") ? trimmed : null;
}

function parseListLine(line) {
  const trimmed = line.trim();
  if (!trimmed || trimmed.startsWith("#")) return null;

  const [flag = "", id = "", url = ""] = trimmed.split(",");
  if (!/^\d+$/.test(id.trim())) return null;

  return {
    id: id.trim(),
    checked: flag.trim() === "1",
    externalSolutionUrl: normalizeUrl(url)
  };
}

function problemTier(level) {
  if (level == null) return null;
  if (level >= 16) return "platinum";
  if (level >= 11) return "gold";
  if (level >= 6) return "silver";
  return "bronze";
}

async function readJson(file, fallback) {
  try {
    return JSON.parse(await fs.readFile(file, "utf8"));
  } catch {
    return fallback;
  }
}

async function readProblemCatalog() {
  const [baseProblems, extraProblems] = await Promise.all([
    readJson(path.join(DATA_DIR, "problems.json"), []),
    readJson(path.join(DATA_DIR, "problems-extra.json"), [])
  ]);
  return [...baseProblems, ...extraProblems];
}

async function main() {
  await fs.mkdir(DATA_DIR, { recursive: true });
  await fs.mkdir(DOCS_DIR, { recursive: true });

  const [treeBody, appProblems, meta] = await Promise.all([
    get(TREE_URL),
    readProblemCatalog(),
    readJson(path.join(DATA_DIR, "problems-meta.json"), {})
  ]);

  const tree = JSON.parse(treeBody).tree ?? [];
  const listPaths = tree
    .filter((entry) => /^algorithms\/[^/]+\/list\.md$/.test(entry.path))
    .map((entry) => entry.path)
    .sort();

  const solutionById = new Map();
  for (const entry of tree) {
    const match = entry.path.match(/^solution\/([^/]+)\/(\d+)\/.+\.(py|cpp|java|c|cc|js|ts|kt|go|rs)$/);
    if (!match) continue;
    const [, categorySlug, id] = match;
    if (!solutionById.has(id)) solutionById.set(id, new Set());
    solutionById.get(id).add(categorySlug);
  }

  const listedById = new Map();
  for (const listPath of listPaths) {
    const categorySlug = listPath.split("/")[1];
    const content = await get(`${RAW_BASE}/${listPath}`);
    for (const line of content.split(/\r?\n/)) {
      const parsed = parseListLine(line);
      if (!parsed) continue;

      if (!listedById.has(parsed.id)) {
        listedById.set(parsed.id, {
          id: parsed.id,
          categories: new Set(),
          checkedInList: false,
          externalSolutionUrls: new Set()
        });
      }

      const item = listedById.get(parsed.id);
      item.categories.add(categorySlug);
      item.checkedInList = item.checkedInList || parsed.checked;
      if (parsed.externalSolutionUrl) item.externalSolutionUrls.add(parsed.externalSolutionUrl);
    }
  }

  const appIds = new Set(appProblems.map((problem) => String(problem.id)));
  const appSlugs = new Set(appProblems.map((problem) => problem.slug));
  const currentAppProblems = appIds.size;
  const additionalNeeded = Math.max(0, TARGET_PROBLEM_COUNT - currentAppProblems);

  const candidates = [...listedById.values()]
    .filter((item) => !appIds.has(item.id))
    .map((item) => {
      const categories = [...item.categories].sort();
      const level = meta[item.id]?.level ?? null;
      const hasRepoSolution = solutionById.has(item.id);
      const hasExternalSolution = item.externalSolutionUrls.size > 0;
      const status = hasRepoSolution
        ? "repo_solution_ready"
        : hasExternalSolution
          ? "external_solution_candidate"
          : "needs_oracle";

      return {
        id: item.id,
        slug: `${categories[0]}-${item.id}`,
        categories,
        checkedInList: item.checkedInList,
        hasRepoSolution,
        repoSolutionCategories: hasRepoSolution ? [...solutionById.get(item.id)].sort() : [],
        hasExternalSolution,
        externalSolutionUrls: [...item.externalSolutionUrls].sort(),
        solvedLevel: level,
        solvedTier: problemTier(level),
        status
      };
    })
    .sort((a, b) => Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug));

  const selectedForDex = candidates.slice(0, additionalNeeded);
  const statusCounts = candidates.reduce((acc, candidate) => {
    acc[candidate.status] = (acc[candidate.status] ?? 0) + 1;
    return acc;
  }, {});
  const tierCounts = selectedForDex.reduce((acc, candidate) => {
    const key = candidate.solvedTier ?? "unknown";
    acc[key] = (acc[key] ?? 0) + 1;
    return acc;
  }, {});

  const listedSlugMatchesApp = [...listedById.values()].filter((item) =>
    [...item.categories].some((category) => appSlugs.has(`${category}-${item.id}`))
  ).length;

  const audit = {
    generatedAt: new Date().toISOString(),
    source: {
      repository: `${OWNER}/${REPO}`,
      ref: REF,
      treeUrl: TREE_URL
    },
    summary: {
      targetProblemCount: TARGET_PROBLEM_COUNT,
      currentAppProblems,
      additionalNeeded,
      algorithmListFiles: listPaths.length,
      algorithmListedUniqueProblems: listedById.size,
      remoteSolutionUniqueProblems: solutionById.size,
      listedProblemsAlreadyInAppById: listedById.size - candidates.length,
      listedSlugMatchesApp,
      expansionCandidates: candidates.length,
      selectedForDex: selectedForDex.length,
      statusCounts,
      selectedTierCounts: tierCounts
    },
    selectedForDex,
    candidates
  };

  await fs.writeFile(
    path.join(DATA_DIR, "problem-expansion-candidates.json"),
    JSON.stringify(audit, null, 2),
    "utf8"
  );

  const lines = [
    "# 문제 확장 후보 감사 결과",
    "",
    `생성 시각: ${audit.generatedAt}`,
    "",
    "## 요약",
    "",
    `- 목표 문제 수: ${TARGET_PROBLEM_COUNT}`,
    `- 현재 앱 문제 수: ${currentAppProblems}`,
    `- 추가 필요 문제 수: ${additionalNeeded}`,
    `- algorithms/list.md 기준 unique 후보: ${listedById.size}`,
    `- 현재 앱에 없는 후보: ${candidates.length}`,
    `- 1차 도감 편입 후보: ${selectedForDex.length}`,
    "",
    "## 후보 상태",
    "",
    `- repo_solution_ready: ${statusCounts.repo_solution_ready ?? 0}`,
    `- external_solution_candidate: ${statusCounts.external_solution_candidate ?? 0}`,
    `- needs_oracle: ${statusCounts.needs_oracle ?? 0}`,
    "",
    "## 1차 편입 후보 solved.ac 티어",
    "",
    `- bronze: ${tierCounts.bronze ?? 0}`,
    `- silver: ${tierCounts.silver ?? 0}`,
    `- gold: ${tierCounts.gold ?? 0}`,
    `- platinum: ${tierCounts.platinum ?? 0}`,
    `- unknown: ${tierCounts.unknown ?? 0}`,
    "",
    "## 우선 확인할 후보 예시",
    "",
    "| BOJ | 대표 분류 | 상태 | 외부 풀이 |",
    "|---|---|---|---|",
    ...selectedForDex.slice(0, 30).map((candidate) => {
      const url = candidate.externalSolutionUrls[0] ?? "";
      return `| ${candidate.id} | ${candidate.categories[0]} | ${candidate.status} | ${url ? "있음" : "없음"} |`;
    }),
    "",
    "전체 후보는 `data/problem-expansion-candidates.json`에서 확인한다.",
    ""
  ];

  await fs.writeFile(path.join(DOCS_DIR, "problem-expansion-audit.md"), lines.join("\n"), "utf8");

  console.log(`[problem-expansion] app problems: ${currentAppProblems}`);
  console.log(`[problem-expansion] target: ${TARGET_PROBLEM_COUNT}, additional needed: ${additionalNeeded}`);
  console.log(`[problem-expansion] listed unique problems: ${listedById.size}`);
  console.log(`[problem-expansion] candidates not in app: ${candidates.length}`);
  console.log(`[problem-expansion] status counts: ${JSON.stringify(statusCounts)}`);
  console.log("[problem-expansion] wrote data/problem-expansion-candidates.json");
  console.log("[problem-expansion] wrote docs/problem-expansion-audit.md");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
