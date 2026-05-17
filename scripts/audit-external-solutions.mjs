import fs from "node:fs/promises";
import https from "node:https";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT, "data");
const DOCS_DIR = path.join(ROOT, "docs");
const INPUT = path.join(DATA_DIR, "problem-expansion-candidates.json");
const OUTPUT = path.join(DATA_DIR, "external-solution-audit.json");
const DOC_OUTPUT = path.join(DOCS_DIR, "external-solution-audit.md");

const LANG_BY_EXT = {
  ".py": "python",
  ".cpp": "cpp",
  ".cc": "cpp",
  ".cxx": "cpp",
  ".java": "java",
  ".js": "javascript",
  ".ts": "typescript",
  ".kt": "kotlin",
  ".go": "go",
  ".rs": "rust",
  ".c": "c"
};

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

function parseGithubTreeUrl(url) {
  const match = url.match(/^https:\/\/github\.com\/([^/]+)\/([^/]+)\/tree\/([^/]+)\/(.+)$/);
  if (!match) return null;
  return {
    owner: match[1],
    repo: match[2],
    ref: match[3],
    path: match[4]
  };
}

function classifyReadiness(files) {
  const languages = new Set(files.map((file) => file.lang));
  if (languages.has("python") || languages.has("cpp")) return "runtime_ready";
  if (languages.has("java")) return "needs_java_runtime_or_port";
  if (files.length > 0) return "needs_runtime_or_port";
  return "missing_solution_files";
}

async function fetchDirectoryFiles(source) {
  const apiUrl = `https://api.github.com/repos/${source.owner}/${source.repo}/contents/${source.path}?ref=${source.ref}`;
  const entries = JSON.parse(await get(apiUrl));
  const files = Array.isArray(entries) ? entries : [entries];

  return files
    .filter((entry) => entry.type === "file")
    .map((entry) => {
      const ext = path.extname(entry.name).toLowerCase();
      const lang = LANG_BY_EXT[ext] ?? null;
      return {
        name: entry.name,
        path: entry.path,
        lang,
        size: entry.size,
        htmlUrl: entry.html_url,
        downloadUrl: entry.download_url
      };
    })
    .filter((entry) => entry.lang);
}

async function main() {
  await fs.mkdir(DATA_DIR, { recursive: true });
  await fs.mkdir(DOCS_DIR, { recursive: true });

  const expansion = JSON.parse(await fs.readFile(INPUT, "utf8"));
  const candidates = expansion.candidates.filter((candidate) => candidate.status === "external_solution_candidate");
  const audited = [];

  for (const candidate of candidates) {
    const sources = [];
    for (const url of candidate.externalSolutionUrls) {
      const source = parseGithubTreeUrl(url);
      if (!source) {
        sources.push({ url, ok: false, error: "unsupported_url" });
        continue;
      }

      try {
        const files = await fetchDirectoryFiles(source);
        sources.push({
          url,
          ok: true,
          repository: `${source.owner}/${source.repo}`,
          ref: source.ref,
          path: source.path,
          files,
          languages: [...new Set(files.map((file) => file.lang))].sort(),
          readiness: classifyReadiness(files)
        });
      } catch (error) {
        sources.push({ url, ok: false, error: error.message });
      }
    }

    const files = sources.flatMap((source) => source.files ?? []);
    audited.push({
      id: candidate.id,
      slug: candidate.slug,
      categories: candidate.categories,
      titleKo: candidate.titleKo ?? null,
      solvedLevel: candidate.solvedLevel ?? null,
      solvedTier: candidate.solvedTier ?? null,
      sources,
      languages: [...new Set(files.map((file) => file.lang))].sort(),
      readiness: classifyReadiness(files)
    });

    console.log(`[external-solutions] ${candidate.id} ${audited[audited.length - 1].readiness}`);
  }

  const readinessCounts = audited.reduce((acc, item) => {
    acc[item.readiness] = (acc[item.readiness] ?? 0) + 1;
    return acc;
  }, {});
  const languageCounts = audited.reduce((acc, item) => {
    for (const lang of item.languages) acc[lang] = (acc[lang] ?? 0) + 1;
    return acc;
  }, {});

  const output = {
    generatedAt: new Date().toISOString(),
    summary: {
      externalCandidates: candidates.length,
      readinessCounts,
      languageCounts
    },
    candidates: audited
  };

  await fs.writeFile(OUTPUT, JSON.stringify(output, null, 2), "utf8");

  const lines = [
    "# 외부 풀이 후보 감사 결과",
    "",
    `생성 시각: ${output.generatedAt}`,
    "",
    "## 요약",
    "",
    `- 외부 풀이 후보: ${candidates.length}`,
    `- Python/C++ 즉시 런타임 가능: ${readinessCounts.runtime_ready ?? 0}`,
    `- Java 런타임 또는 포팅 필요: ${readinessCounts.needs_java_runtime_or_port ?? 0}`,
    `- 기타 런타임 또는 포팅 필요: ${readinessCounts.needs_runtime_or_port ?? 0}`,
    `- 풀이 파일 확인 실패: ${readinessCounts.missing_solution_files ?? 0}`,
    "",
    "## 언어 분포",
    "",
    ...Object.entries(languageCounts)
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([lang, count]) => `- ${lang}: ${count}`),
    "",
    "## 후보 목록",
    "",
    "| BOJ | 대표 분류 | 언어 | 준비 상태 |",
    "|---|---|---|---|",
    ...audited.map((item) => `| ${item.id} | ${item.categories[0]} | ${item.languages.join(", ") || "-"} | ${item.readiness} |`),
    "",
    "전체 상세 파일과 원본 링크는 `data/external-solution-audit.json`에서 확인한다.",
    ""
  ];

  await fs.writeFile(DOC_OUTPUT, lines.join("\n"), "utf8");
  console.log("[external-solutions] wrote data/external-solution-audit.json");
  console.log("[external-solutions] wrote docs/external-solution-audit.md");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
