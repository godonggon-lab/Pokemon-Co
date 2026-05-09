import fs from "node:fs";
import path from "node:path";

const problems = JSON.parse(fs.readFileSync("data/problems.json", "utf8"));
const statements = JSON.parse(fs.readFileSync("data/problems-statements.json", "utf8"));
const overridesDir = path.join("harness", "overrides");

const riskWeights = new Map([
  ["graph_traversal", 100],
  ["dynamic_programming_1", 95],
  ["dynamic_programming_2", 95],
  ["dynamic_programming_on_trees", 95],
  ["shortest_path", 92],
  ["minimum_spanning_tree", 90],
  ["two_pointer", 88],
  ["binary_search", 86],
  ["backtracking", 84],
  ["simulation", 82],
  ["prefix_sum", 80],
  ["data_structure", 78],
  ["data_structure2", 78],
  ["greedy", 72],
  ["brute_force", 65],
  ["implementation", 55],
  ["string", 50],
  ["math", 45],
]);

const rows = problems.map((problem) => {
  const sampleCount = Array.isArray(statements[problem.id]?.samples)
    ? statements[problem.id].samples.length
    : 0;
  const overridePath = path.join(overridesDir, `${problem.slug}.py`);
  const hasOverride = fs.existsSync(overridePath);
  const riskWeight = riskWeights.get(problem.categorySlug) ?? 40;
  const sourceLangs = (problem.sources ?? []).map((source) => source.lang);

  return {
    slug: problem.slug,
    id: problem.id,
    category: problem.categorySlug,
    sampleCount,
    hasOverride,
    sourceLangs,
    score: riskWeight + Math.max(0, 4 - sampleCount) * 10,
  };
});

const missing = rows.filter((row) => row.sampleCount === 0 && !row.hasOverride);
const sampleOnly = rows.filter((row) => row.sampleCount > 0 && !row.hasOverride);
const highRiskSampleOnly = sampleOnly
  .filter((row) => (riskWeights.get(row.category) ?? 0) >= 78)
  .sort((a, b) => b.score - a.score || a.sampleCount - b.sampleCount || a.id - b.id);

const summary = {
  total: rows.length,
  judgeReady: rows.length - missing.length,
  missingCases: missing.length,
  overrides: rows.filter((row) => row.hasOverride).length,
  sampleOnly: sampleOnly.length,
  highRiskSampleOnly: highRiskSampleOnly.length,
  topCandidates: highRiskSampleOnly.slice(0, 50),
};

console.log(JSON.stringify(summary, null, 2));
