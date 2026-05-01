// BOJ 원문 statement 로더 (Wayback Machine 페치 결과).

import statementsJson from "@/data/problems-statements.json";

export type ProblemStatement = {
  title: string;
  description: string;
  input: string;
  output: string;
  limit: string;
  hint: string;
  samples: { idx: number; in: string; out: string }[];
  limits: { timeLimitMs: number | null; memoryLimitMb: number | null };
  snapshotTs: string;
};

const STATEMENTS = statementsJson as Record<string, ProblemStatement | { _failed: true }>;

export function getStatement(problemId: string): ProblemStatement | null {
  const s = STATEMENTS[problemId];
  if (!s || (s as any)._failed) return null;
  return s as ProblemStatement;
}
