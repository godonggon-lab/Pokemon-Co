import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const PHASE_DIR = path.join(ROOT, "docs", "phases");

const TARGET_COUNT = Number(process.env.BATCH_SIZE ?? 100);
const OUTPUT = path.join(DATA_DIR, "problem-expansion-batch-02.json");
const DOC_OUTPUT = path.join(PHASE_DIR, "phase-13-batch-02-100-candidates.md");

const CATEGORY_PRIORITY = new Map([
  ["string", 10],
  ["math", 12],
  ["implementation", 14],
  ["prefix_sum", 16],
  ["greedy", 18],
  ["brute_force", 20],
  ["data_structure", 24],
  ["data_structure2", 26],
  ["binary_search", 28],
  ["two_pointer", 30],
  ["dynamic_programming_1", 36],
  ["graph_traversal", 38],
  ["backtracking", 42],
  ["shortest_path", 46],
  ["tree", 48],
  ["divide_and_conquer", 50],
  ["dynamic_programming_2", 54],
  ["simulation", 58],
  ["minimum_spanning_tree", 62],
  ["topological_sorting", 64]
]);

function categoryScore(candidate) {
  return Math.min(...candidate.categories.map((category) => CATEGORY_PRIORITY.get(category) ?? 100));
}

function statusScore(candidate, externalAuditById) {
  const external = externalAuditById.get(candidate.id);
  if (external?.readiness === "runtime_ready") return 0;
  if (candidate.status === "external_solution_candidate") return 20;
  return 40;
}

function importReadiness(candidate, externalAuditById, statements) {
  const external = externalAuditById.get(candidate.id);
  const statement = statements[candidate.id];
  const statementReady = Boolean(statement && !statement._failed);
  const hasRuntimeSource = external?.readiness === "runtime_ready";

  if (hasRuntimeSource && statementReady) return "ready_for_override";
  if (hasRuntimeSource) return "needs_statement";
  if (statementReady) return "needs_oracle";
  return "needs_statement_and_oracle";
}

function batchLane(candidate, externalAuditById) {
  const external = externalAuditById.get(candidate.id);
  if (external?.readiness === "runtime_ready") return "external_runtime";
  if (candidate.status === "external_solution_candidate") return "external_java_or_port";
  return "manual_oracle";
}

async function readJson(file, fallback) {
  try {
    return JSON.parse(await fs.readFile(file, "utf8"));
  } catch {
    return fallback;
  }
}

async function main() {
  await fs.mkdir(DATA_DIR, { recursive: true });
  await fs.mkdir(PHASE_DIR, { recursive: true });

  const [expansion, externalAudit, statements] = await Promise.all([
    readJson(path.join(DATA_DIR, "problem-expansion-candidates.json"), null),
    readJson(path.join(DATA_DIR, "external-solution-audit.json"), { candidates: [] }),
    readJson(path.join(DATA_DIR, "problems-statements.json"), {})
  ]);
  if (!expansion) throw new Error("missing data/problem-expansion-candidates.json");

  const externalAuditById = new Map(externalAudit.candidates.map((candidate) => [candidate.id, candidate]));
  const candidates = [...expansion.candidates]
    .sort((a, b) => {
      const sa = statusScore(a, externalAuditById);
      const sb = statusScore(b, externalAuditById);
      if (sa !== sb) return sa - sb;

      const ca = categoryScore(a);
      const cb = categoryScore(b);
      if (ca !== cb) return ca - cb;

      return Number(a.id) - Number(b.id) || a.slug.localeCompare(b.slug);
    })
    .slice(0, TARGET_COUNT)
    .map((candidate) => {
      const external = externalAuditById.get(candidate.id);
      const statement = statements[candidate.id];
      return {
        id: candidate.id,
        slug: candidate.slug,
        primaryCategory: candidate.categories[0],
        categories: candidate.categories,
        lane: batchLane(candidate, externalAuditById),
        status: candidate.status,
        readiness: importReadiness(candidate, externalAuditById, statements),
        title: statement && !statement._failed ? statement.title : null,
        statementReady: Boolean(statement && !statement._failed),
        sampleCount: statement && !statement._failed ? statement.samples.length : 0,
        externalReadiness: external?.readiness ?? null,
        externalLanguages: external?.languages ?? [],
        externalSourceFiles: external?.sources?.flatMap((source) => source.files ?? []) ?? [],
        requiredWork:
          external?.readiness === "runtime_ready"
            ? ["statement 확보", "외부 정답 self-judge", "edge/fuzz override 작성", "problems-extra 편입"]
            : ["statement 확보", "Python/C++ oracle 작성", "edge/fuzz override 작성", "problems-extra 편입"]
      };
    });

  const laneCounts = candidates.reduce((acc, candidate) => {
    acc[candidate.lane] = (acc[candidate.lane] ?? 0) + 1;
    return acc;
  }, {});
  const readinessCounts = candidates.reduce((acc, candidate) => {
    acc[candidate.readiness] = (acc[candidate.readiness] ?? 0) + 1;
    return acc;
  }, {});
  const categoryCounts = candidates.reduce((acc, candidate) => {
    acc[candidate.primaryCategory] = (acc[candidate.primaryCategory] ?? 0) + 1;
    return acc;
  }, {});

  const output = {
    generatedAt: new Date().toISOString(),
    phase: "13-batch-02",
    targetCount: TARGET_COUNT,
    serviceReady: false,
    strategy: "external runtime candidates first, then easy manual-oracle categories",
    summary: {
      selected: candidates.length,
      laneCounts,
      readinessCounts,
      categoryCounts
    },
    candidates
  };

  await fs.writeFile(OUTPUT, JSON.stringify(output, null, 2), "utf8");

  const lines = [
    "# Phase 13 Batch 02. 100개 확장 후보",
    "",
    "## 목표",
    "",
    "포켓몬 1025종 목표를 향해 다음 편입 후보를 100개 단위로 크게 잡는다.",
    "",
    "이 문서는 즉시 서비스 편입 목록이 아니라, 100개 후보를 작업 lane별로 나눈 실행 대기열이다.",
    "",
    "## 선정 전략",
    "",
    "1. 외부 Python/C++ 풀이가 있는 후보를 우선한다.",
    "2. 이후 직접 oracle 작성이 쉬운 유형을 우선한다.",
    "3. 같은 우선순위에서는 BOJ 번호가 낮은 문제를 먼저 둔다.",
    "",
    "## 요약",
    "",
    `- 후보 수: ${candidates.length}`,
    `- external_runtime: ${laneCounts.external_runtime ?? 0}`,
    `- external_java_or_port: ${laneCounts.external_java_or_port ?? 0}`,
    `- manual_oracle: ${laneCounts.manual_oracle ?? 0}`,
    "",
    "## 준비 상태",
    "",
    ...Object.entries(readinessCounts)
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([key, value]) => `- ${key}: ${value}`),
    "",
    "## 후보 목록",
    "",
    "| # | BOJ | slug | lane | readiness | sample |",
    "|---:|---|---|---|---|---:|",
    ...candidates.map((candidate, index) =>
      `| ${index + 1} | ${candidate.id} | ${candidate.slug} | ${candidate.lane} | ${candidate.readiness} | ${candidate.sampleCount} |`
    ),
    "",
    "## 실행 순서",
    "",
    "1. `external_runtime` 중 statement가 있는 문제부터 10개 편입한다.",
    "2. statement가 없는 문제는 `fetch-boj-statements.mjs --only=...`로 먼저 확보한다.",
    "3. `manual_oracle`은 쉬운 유형부터 20개씩 oracle/override를 작성한다.",
    "4. 각 묶음마다 `verify-judge-overrides`, `judge:coverage`, `next build`를 통과시킨다.",
    "",
    "## 출력",
    "",
    "- `data/problem-expansion-batch-02.json`",
    ""
  ];

  await fs.writeFile(DOC_OUTPUT, lines.join("\n"), "utf8");
  console.log(`[batch-02] selected: ${candidates.length}`);
  console.log(`[batch-02] lanes: ${JSON.stringify(laneCounts)}`);
  console.log(`[batch-02] readiness: ${JSON.stringify(readinessCounts)}`);
  console.log("[batch-02] wrote data/problem-expansion-batch-02.json");
  console.log("[batch-02] wrote docs/phases/phase-13-batch-02-100-candidates.md");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
