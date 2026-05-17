import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const PHASE_DIR = path.join(ROOT, "docs", "phases");
const INPUT = path.join(DATA_DIR, "external-solution-audit.json");
const OUTPUT = path.join(DATA_DIR, "problem-expansion-batch-01.json");
const DOC_OUTPUT = path.join(PHASE_DIR, "phase-13-batch-01-external-runtime.md");

async function main() {
  await fs.mkdir(DATA_DIR, { recursive: true });
  await fs.mkdir(PHASE_DIR, { recursive: true });

  const audit = JSON.parse(await fs.readFile(INPUT, "utf8"));
  const candidates = audit.candidates
    .filter((candidate) => candidate.readiness === "runtime_ready")
    .sort((a, b) => Number(a.id) - Number(b.id));

  const batch = {
    generatedAt: new Date().toISOString(),
    phase: "13-batch-01",
    title: "외부 풀이 Python/C++ 런타임 후보 1차 편입",
    serviceReady: false,
    reasonNotReady: "문제 본문 요약, sample/edge/fuzz case, oracle 검증이 아직 필요하다.",
    summary: {
      targetCount: candidates.length,
      source: "data/external-solution-audit.json",
      readiness: "runtime_ready"
    },
    candidates: candidates.map((candidate) => ({
      id: candidate.id,
      slug: candidate.slug,
      primaryCategory: candidate.categories[0],
      categories: candidate.categories,
      languages: candidate.languages,
      sourceFiles: candidate.sources.flatMap((source) =>
        (source.files ?? []).map((file) => ({
          lang: file.lang,
          name: file.name,
          htmlUrl: file.htmlUrl,
          downloadUrl: file.downloadUrl
        }))
      ),
      requiredBeforeImport: [
        "BOJ 원문 링크와 앱용 문제 요약 작성",
        "sample input/output 확보",
        "정답 코드가 Python/C++ 런타임에서 통과하는지 확인",
        "문제별 edge/fuzz case 작성",
        "필요 시 TLE/stress case 작성",
        "data/problems.json 편입 후 monster-map 재생성"
      ]
    }))
  };

  await fs.writeFile(OUTPUT, JSON.stringify(batch, null, 2), "utf8");

  const lines = [
    "# Phase 13 Batch 01. 외부 풀이 런타임 후보",
    "",
    "## 목표",
    "",
    "외부 풀이 링크가 있고, 그중 Python 또는 C++ 코드가 확인된 문제를 1차 편입 후보로 묶는다.",
    "",
    "이 batch는 아직 서비스 편입 완료가 아니다. 정답 코드 파일이 확인되었을 뿐이고, 문제 요약/예제/edge/fuzz 검증을 거쳐야 한다.",
    "",
    "## 후보 요약",
    "",
    `- 후보 수: ${batch.summary.targetCount}`,
    "- 기준: `data/external-solution-audit.json`에서 `runtime_ready`인 문제",
    "- 상태: 편입 준비 후보",
    "",
    "## 후보 목록",
    "",
    "| BOJ | slug | 대표 분류 | 언어 |",
    "|---|---|---|---|",
    ...batch.candidates.map((candidate) =>
      `| ${candidate.id} | ${candidate.slug} | ${candidate.primaryCategory} | ${candidate.languages.join(", ")} |`
    ),
    "",
    "## 편입 전 필수 작업",
    "",
    "1. BOJ 원문 링크와 앱용 문제 요약을 작성한다.",
    "2. sample input/output을 확보한다.",
    "3. 외부 정답 코드를 Python/C++ Docker runner에서 실행 검증한다.",
    "4. 문제별 edge/fuzz case를 작성한다.",
    "5. 시간복잡도 함정이 있는 문제는 stress case를 추가한다.",
    "6. 검증 통과 후 `data/problems.json`에 편입하고 `npm run data:map`을 실행한다.",
    "",
    "## 실행 결과",
    "",
    `- 생성 시각: ${batch.generatedAt}`,
    "- 출력: `data/problem-expansion-batch-01.json`",
    "",
    "## 다음 단계",
    "",
    "이 batch에서 쉬운 문제부터 5개를 골라 실제 문제 요약과 override를 작성한다. 첫 5개는 입출력 안정성과 구현 난이도를 기준으로 고른다.",
    ""
  ];

  await fs.writeFile(DOC_OUTPUT, lines.join("\n"), "utf8");
  console.log(`[batch-01] candidates: ${batch.summary.targetCount}`);
  console.log("[batch-01] wrote data/problem-expansion-batch-01.json");
  console.log("[batch-01] wrote docs/phases/phase-13-batch-01-external-runtime.md");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
