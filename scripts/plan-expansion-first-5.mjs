import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const PHASE_DIR = path.join(ROOT, "docs", "phases");

const FIRST_IDS = ["4949", "11256", "11441", "1697", "2156"];

async function main() {
  const [batch, statements] = await Promise.all([
    fs.readFile(path.join(DATA_DIR, "problem-expansion-batch-01.json"), "utf8").then(JSON.parse),
    fs.readFile(path.join(DATA_DIR, "problems-statements.json"), "utf8").then(JSON.parse)
  ]);

  const byId = new Map(batch.candidates.map((candidate) => [candidate.id, candidate]));
  const candidates = FIRST_IDS.map((id) => {
    const candidate = byId.get(id);
    const statement = statements[id];
    if (!candidate) throw new Error(`batch candidate not found: ${id}`);

    return {
      id,
      slug: candidate.slug,
      primaryCategory: candidate.primaryCategory,
      languages: candidate.languages,
      sourceFiles: candidate.sourceFiles,
      statementReady: Boolean(statement && !statement._failed),
      title: statement && !statement._failed ? statement.title : null,
      sampleCount: statement && !statement._failed ? statement.samples.length : 0,
      limits: statement && !statement._failed ? statement.limits : null,
      nextAction: "앱용 문제 요약과 override를 작성한 뒤 정답 코드 실행 검증"
    };
  });

  const output = {
    generatedAt: new Date().toISOString(),
    phase: "13-first-5",
    serviceReady: false,
    candidates
  };

  await fs.writeFile(
    path.join(DATA_DIR, "problem-expansion-first-5.json"),
    JSON.stringify(output, null, 2),
    "utf8"
  );

  const lines = [
    "# Phase 13 First 5. 첫 편입 검토 문제",
    "",
    "## 목표",
    "",
    "외부 풀이가 있고 statement/sample 확보가 된 쉬운 문제 5개를 골라 실제 편입 검토를 시작한다.",
    "",
    "## 선정 기준",
    "",
    "- Python 또는 C++ 정답 코드가 있다.",
    "- Wayback 기반 statement/sample 확보가 됐다.",
    "- 문제 유형이 비교적 명확해서 edge/fuzz case를 작성하기 쉽다.",
    "",
    "## 후보",
    "",
    "| BOJ | 제목 | slug | 언어 | sample | 상태 |",
    "|---|---|---|---|---:|---|",
    ...candidates.map((candidate) =>
      `| ${candidate.id} | ${candidate.title ?? ""} | ${candidate.slug} | ${candidate.languages.join(", ")} | ${candidate.sampleCount} | ${candidate.statementReady ? "statement 확보" : "statement 필요"} |`
    ),
    "",
    "## 다음 작업",
    "",
    "1. 각 문제의 BOJ 원문을 그대로 복제하지 않고 앱용 요약을 작성한다.",
    "2. 외부 정답 코드를 로컬 oracle 후보로 저장할지, 직접 oracle을 새로 작성할지 결정한다.",
    "3. sample case를 먼저 통과시킨다.",
    "4. edge/fuzz case를 작성한다.",
    "5. 5개 모두 통과하면 `data/problems.json` 편입 방식을 확정한다.",
    "",
    "## 실행 결과",
    "",
    `- 생성 시각: ${output.generatedAt}`,
    "- 출력: `data/problem-expansion-first-5.json`",
    ""
  ];

  await fs.writeFile(
    path.join(PHASE_DIR, "phase-13-first-5.md"),
    lines.join("\n"),
    "utf8"
  );

  console.log(`[first-5] candidates: ${candidates.length}`);
  console.log("[first-5] wrote data/problem-expansion-first-5.json");
  console.log("[first-5] wrote docs/phases/phase-13-first-5.md");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
