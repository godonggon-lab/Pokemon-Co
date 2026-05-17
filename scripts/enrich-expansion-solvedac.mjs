import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const DOCS_DIR = path.join(ROOT, "docs");
const AUDIT_PATH = path.join(DATA_DIR, "problem-expansion-candidates.json");
const DOC_PATH = path.join(DOCS_DIR, "problem-expansion-audit.md");

const TIER_NAMES = [
  "Unrated",
  "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
  "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I",
  "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I",
  "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I",
  "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
  "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I"
];

function problemTier(level) {
  if (level == null) return null;
  if (level >= 16) return "platinum";
  if (level >= 11) return "gold";
  if (level >= 6) return "silver";
  return "bronze";
}

async function fetchJson(url, attempt = 0) {
  try {
    const response = await fetch(url, {
      headers: {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36",
        accept: "application/json"
      }
    });
    if (response.status === 404) return null;
    if (!response.ok) {
      const body = await response.text();
      const error = new Error(`HTTP ${response.status}`);
      error.status = response.status;
      error.body = body.slice(0, 200);
      throw error;
    }
    return await response.json();
  } catch (error) {
    if (attempt >= 3) throw error;
    await new Promise((resolve) => setTimeout(resolve, 700 * (attempt + 1)));
    return fetchJson(url, attempt + 1);
  }
}

function recount(audit) {
  const selectedForDex = audit.candidates.slice(0, audit.summary.additionalNeeded);
  const statusCounts = audit.candidates.reduce((acc, candidate) => {
    acc[candidate.status] = (acc[candidate.status] ?? 0) + 1;
    return acc;
  }, {});
  const selectedTierCounts = selectedForDex.reduce((acc, candidate) => {
    const key = candidate.solvedTier ?? "unknown";
    acc[key] = (acc[key] ?? 0) + 1;
    return acc;
  }, {});

  audit.selectedForDex = selectedForDex;
  audit.summary.selectedForDex = selectedForDex.length;
  audit.summary.shortageToTarget = Math.max(0, audit.summary.additionalNeeded - selectedForDex.length);
  audit.summary.statusCounts = statusCounts;
  audit.summary.selectedTierCounts = selectedTierCounts;
  audit.summary.solvedAcKnownCandidates = audit.candidates.filter((candidate) => candidate.solvedLevel != null).length;
  audit.summary.solvedAcUnknownCandidates = audit.candidates.filter((candidate) => candidate.solvedLevel == null).length;
}

async function rewriteDoc(audit) {
  const { summary } = audit;
  const statusCounts = summary.statusCounts ?? {};
  const tierCounts = summary.selectedTierCounts ?? {};
  const lines = [
    "# 문제 확장 후보 감사 결과",
    "",
    `생성 시각: ${audit.generatedAt}`,
    `난이도 보강 시각: ${audit.solvedAcEnrichedAt ?? "미실행"}`,
    "",
    "## 요약",
    "",
    `- 목표 문제 수: ${summary.targetProblemCount}`,
    `- 현재 앱 문제 수: ${summary.currentAppProblems}`,
    `- 추가 필요 문제 수: ${summary.additionalNeeded}`,
    `- algorithms/list.md 기준 unique 후보: ${summary.algorithmListedUniqueProblems}`,
    `- 현재 앱에 없는 후보: ${summary.expansionCandidates}`,
    `- 1차 도감 편입 후보: ${summary.selectedForDex}`,
    `- 목표 대비 부족분: ${summary.shortageToTarget ?? 0}`,
    `- solved.ac 확인 완료 후보: ${summary.solvedAcKnownCandidates ?? 0}`,
    `- solved.ac unknown 후보: ${summary.solvedAcUnknownCandidates ?? summary.selectedForDex}`,
    `- solved.ac 수집 실패 횟수: ${audit.solvedAcFailures?.length ?? 0}`,
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
    "| BOJ | 제목 | 대표 분류 | 티어 | 상태 | 외부 풀이 |",
    "|---|---|---|---|---|---|",
    ...audit.selectedForDex.slice(0, 30).map((candidate) => {
      const url = candidate.externalSolutionUrls[0] ?? "";
      return `| ${candidate.id} | ${candidate.titleKo ?? ""} | ${candidate.categories[0]} | ${candidate.solvedTier ?? "unknown"} | ${candidate.status} | ${url ? "있음" : "없음"} |`;
    }),
    "",
    "전체 후보는 `data/problem-expansion-candidates.json`에서 확인한다.",
    ""
  ];

  await fs.writeFile(DOC_PATH, lines.join("\n"), "utf8");
}

async function main() {
  const audit = JSON.parse(await fs.readFile(AUDIT_PATH, "utf8"));
  const need = audit.candidates
    .filter((candidate) => candidate.solvedLevel == null)
    .map((candidate) => candidate.id);

  console.log(`[expansion-solvedac] need=${need.length}`);

  const metaById = new Map();
  const failures = [];
  for (let i = 0; i < need.length; i += 100) {
    const chunk = need.slice(i, i + 100);
    try {
      const data = await fetchJson(`https://solved.ac/api/v3/problem/lookup?problemIds=${chunk.join(",")}`);
      if (Array.isArray(data)) {
        for (const problem of data) {
          metaById.set(String(problem.problemId), {
            titleKo: problem.titleKo,
            solvedLevel: problem.level,
            solvedLevelName: TIER_NAMES[problem.level] ?? "Unrated",
            solvedTier: problemTier(problem.level),
            acceptedCount: problem.acceptedUserCount ?? 0,
            averageTries: problem.averageTries ?? 0
          });
        }
      }
    } catch (error) {
      failures.push({
        offset: i,
        status: error.status ?? null,
        message: error.message,
        body: error.body ?? ""
      });
      console.warn(`  ! chunk ${i}-${i + chunk.length - 1}: ${error.message}`);
      if (error.status === 403) break;
    }
    console.log(`  - ${Math.min(i + chunk.length, need.length)}/${need.length}`);
    await new Promise((resolve) => setTimeout(resolve, 800));
  }

  for (const candidate of audit.candidates) {
    const meta = metaById.get(candidate.id);
    if (!meta) continue;
    Object.assign(candidate, meta);
  }

  audit.solvedAcEnrichedAt = new Date().toISOString();
  audit.solvedAcFailures = failures;
  recount(audit);

  await fs.writeFile(AUDIT_PATH, JSON.stringify(audit, null, 2), "utf8");
  await rewriteDoc(audit);

  console.log(`[expansion-solvedac] known=${audit.summary.solvedAcKnownCandidates}`);
  console.log(`[expansion-solvedac] unknown=${audit.summary.solvedAcUnknownCandidates}`);
  console.log(`[expansion-solvedac] selected tiers=${JSON.stringify(audit.summary.selectedTierCounts)}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
