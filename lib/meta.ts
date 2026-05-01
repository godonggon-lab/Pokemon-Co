// solved.ac 메타데이터 로더.
// data/problems-meta.json (build 시 생성)

import metaJson from "@/data/problems-meta.json";
import type { ProblemMeta } from "./flavor";

const META = metaJson as Record<string, ProblemMeta>;

export function getProblemMeta(problemId: string): ProblemMeta | undefined {
  return META[problemId];
}
