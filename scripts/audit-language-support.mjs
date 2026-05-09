import fs from "node:fs";
import { spawnSync } from "node:child_process";

const problems = JSON.parse(fs.readFileSync("data/problems.json", "utf8"));
const apiRoute = fs.readFileSync("app/api/judge/route.ts", "utf8");
const playground = fs.readFileSync("components/ProblemPlayground.tsx", "utf8");
const dockerfile = fs.readFileSync("judge/Dockerfile", "utf8");
const entrypoint = fs.readFileSync("judge/entrypoint.sh", "utf8");

function hasCommand(command) {
  const probe = process.platform === "win32" ? "where.exe" : "command";
  const args = process.platform === "win32" ? [command] : ["-v", command];
  return spawnSync(probe, args, { encoding: "utf8" }).status === 0;
}

function sourceStats() {
  const missingPython = [];
  const missingCpp = [];
  const neitherPythonNorCpp = [];
  let python = 0;
  let cpp = 0;
  let both = 0;
  let oracleAvailable = 0;

  for (const problem of problems) {
    const langs = new Set((problem.sources ?? []).map((source) => source.lang));
    if ((problem.sources ?? []).length > 0) oracleAvailable += 1;
    if (langs.has("python")) python += 1;
    else missingPython.push(problem.slug);
    if (langs.has("cpp")) cpp += 1;
    else missingCpp.push(problem.slug);
    if (langs.has("python") && langs.has("cpp")) both += 1;
    if (!langs.has("python") && !langs.has("cpp")) neitherPythonNorCpp.push(problem.slug);
  }

  return {
    python,
    cpp,
    both,
    oracleAvailable,
    missingPython: missingPython.length,
    missingCpp: missingCpp.length,
    neitherPythonNorCpp: neitherPythonNorCpp.length,
    neitherPythonNorCppSlugs: neitherPythonNorCpp,
  };
}

const runtime = {
  apiAllowsPython: /ALLOWED_LANGS[\s\S]*"python"/.test(apiRoute),
  apiAllowsCpp: /ALLOWED_LANGS[\s\S]*"cpp"/.test(apiRoute),
  playgroundOffersPython: /SUBMIT_LANGS[\s\S]*"python"/.test(playground),
  playgroundOffersCpp: /SUBMIT_LANGS[\s\S]*"cpp"/.test(playground),
  dockerImageInstallsPython: /python3/.test(dockerfile),
  dockerImageInstallsCpp: /\bg\+\+/.test(dockerfile),
  entrypointRunsPython: /python\)\s*[\s\S]*run python main\.py/.test(entrypoint),
  entrypointRunsCpp: /cpp\)\s*[\s\S]*g\+\+/.test(entrypoint),
  localPythonAvailable: hasCommand("python"),
  localGppAvailable: hasCommand("g++"),
  dockerCliAvailable: hasCommand("docker"),
};

const stats = sourceStats();
const allProblemsAcceptPythonCpp =
  runtime.apiAllowsPython &&
  runtime.apiAllowsCpp &&
  runtime.playgroundOffersPython &&
  runtime.playgroundOffersCpp &&
  runtime.dockerImageInstallsPython &&
  runtime.dockerImageInstallsCpp &&
  runtime.entrypointRunsPython &&
  runtime.entrypointRunsCpp;

console.log(JSON.stringify({
  totalProblems: problems.length,
  allProblemsAcceptPythonCpp,
  sourceCoverage: stats,
  runtime,
  notes: [
    "sourceCoverage는 정답/oracle 소스 현황이다. 사용자 제출 가능 여부와는 별개다.",
    "운영에서 C++ 제출을 안정적으로 받으려면 JUDGE_USE_DOCKER=1과 coderunner Docker image가 필요하다.",
    "로컬에서 JUDGE_USE_DOCKER=0으로 C++ 제출을 실행하려면 g++가 설치되어 있어야 한다.",
  ],
}, null, 2));
