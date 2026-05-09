import fs from "node:fs";
import path from "node:path";

const problems = JSON.parse(fs.readFileSync("data/problems.json", "utf8"));
const statements = JSON.parse(fs.readFileSync("data/problems-statements.json", "utf8"));
const overridesDir = path.join("harness", "overrides");

const rows = problems.map((problem) => {
  const statement = statements[problem.id];
  const sampleCount = Array.isArray(statement?.samples) ? statement.samples.length : 0;
  const overridePath = path.join(overridesDir, `${problem.slug}.py`);
  const hasOverride = fs.existsSync(overridePath);
  const oracleLangs = (problem.sources ?? []).map((source) => source.lang);
  return {
    slug: problem.slug,
    id: problem.id,
    category: problem.categorySlug,
    samples: sampleCount,
    override: hasOverride,
    oracleLangs,
    judgeReady: sampleCount > 0 || hasOverride
  };
});

const ready = rows.filter((row) => row.judgeReady);
const missing = rows.filter((row) => !row.judgeReady);
const overrides = rows.filter((row) => row.override);

console.log(JSON.stringify({
  total: rows.length,
  judgeReady: ready.length,
  missingCases: missing.length,
  overrides: overrides.map((row) => row.slug),
  missingCaseSlugs: missing.map((row) => row.slug)
}, null, 2));
