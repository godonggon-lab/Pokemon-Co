// 정적 데이터 로더. Next.js 빌드 타임에 JSON 을 import 해 메모리에 로딩.
// (data/*.json 은 npm run index:boj 로 생성)

import type { Category, Problem } from "./types";
import categoriesJson from "@/data/categories.json";
import problemsJson   from "@/data/problems.json";

export const categories: Category[] = categoriesJson as Category[];
export const problems:   Problem[]  = problemsJson   as Problem[];

const byCatSlug = new Map<string, Category>();
for (const c of categories) byCatSlug.set(c.slug, c);

const byProblemSlug = new Map<string, Problem>();
for (const p of problems) byProblemSlug.set(p.slug, p);

const byCategoryGroup = new Map<string, Problem[]>();
for (const p of problems) {
  const arr = byCategoryGroup.get(p.categorySlug) ?? [];
  arr.push(p);
  byCategoryGroup.set(p.categorySlug, arr);
}

export function getCategory(slug: string): Category | undefined {
  return byCatSlug.get(slug);
}
export function getProblem(slug: string): Problem | undefined {
  return byProblemSlug.get(slug);
}
export function getProblemsOf(categorySlug: string): Problem[] {
  return byCategoryGroup.get(categorySlug) ?? [];
}
