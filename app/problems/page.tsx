import Link from "next/link";
import { categories, problems } from "@/lib/dataset";

export default function ProblemsPage() {
  const byCat = new Map(categories.map((c) => [c.slug, c]));
  return (
    <div className="space-y-6">
      <div>
        <h1 className="section-title flex items-center gap-2">
          <span>📋</span> 전체 문제
          <span className="ml-1 rounded-full bg-amber-500/10 px-2.5 py-0.5 text-sm font-bold text-amber-300">
            {problems.length}
          </span>
        </h1>
        <p className="mt-1 text-sm text-white/40">모든 알고리즘 몬스터를 한눈에 볼 수 있어요</p>
      </div>

      <div className="overflow-hidden rounded-2xl border border-white/[0.06]" style={{ background: "linear-gradient(145deg, #1e1f3b, #1a1b32)" }}>
        <table className="poke-table">
          <thead>
            <tr>
              <th className="px-4 py-3">#</th>
              <th className="px-4 py-3">분류</th>
              <th className="px-4 py-3">언어</th>
              <th className="px-4 py-3">바로가기</th>
            </tr>
          </thead>
          <tbody>
            {problems.map((p) => {
              const cat = byCat.get(p.categorySlug);
              return (
                <tr key={p.slug}>
                  <td className="px-4 py-2.5 font-mono text-white/50">{p.id}</td>
                  <td className="px-4 py-2.5">
                    <span className="font-semibold">{cat?.name_ko ?? p.categorySlug}</span>
                  </td>
                  <td className="px-4 py-2.5 text-white/40">{p.sources.map((s) => s.lang).join(", ")}</td>
                  <td className="px-4 py-2.5">
                    <Link
                      href={`/problem/${p.slug}`}
                      className="inline-flex items-center gap-1 rounded-lg bg-amber-500/10 px-3 py-1 text-xs font-bold text-amber-300 transition-colors hover:bg-amber-500/20"
                    >
                      도전하기 ⚔️
                    </Link>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
