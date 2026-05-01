import Link from "next/link";
import { categories, problems } from "@/lib/dataset";

export default function ProblemsPage() {
  const byCat = new Map(categories.map((c) => [c.slug, c]));
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">전체 문제 ({problems.length})</h1>
      <div className="overflow-hidden rounded-2xl border border-white/10">
        <table className="w-full text-sm">
          <thead className="bg-zinc-900 text-left text-xs uppercase tracking-wider text-zinc-400">
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
                <tr key={p.slug} className="border-t border-white/5 hover:bg-white/5">
                  <td className="px-4 py-2 font-mono">{p.id}</td>
                  <td className="px-4 py-2 text-zinc-300">{cat?.name_ko ?? p.categorySlug}</td>
                  <td className="px-4 py-2 text-zinc-400">{p.sources.map((s) => s.lang).join(", ")}</td>
                  <td className="px-4 py-2">
                    <Link href={`/problem/${p.slug}`} className="text-amber-400 hover:underline">
                      입장 →
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
