import Link from "next/link";
import { notFound } from "next/navigation";
import { categories, getCategory, getProblemsOf } from "@/lib/dataset";
import CategoryGrid from "@/components/CategoryGrid";

export function generateStaticParams() {
  return categories.map((c) => ({ slug: c.slug }));
}

export default function CategoryPage({ params }: { params: { slug: string } }) {
  const cat = getCategory(params.slug);
  if (!cat) notFound();
  const list = getProblemsOf(cat.slug);

  return (
    <div className="space-y-6">
      <div>
        <Link href="/" className="inline-flex items-center gap-1 text-xs text-white/40 transition-colors hover:text-amber-300">
          ← 도감으로
        </Link>
        <h1 className="mt-2 text-3xl font-extrabold">
          {cat.name_ko} <span className="text-sm font-normal text-white/30">/ {cat.type}</span>
        </h1>
        <p className="text-sm text-white/40">{list.length}마리의 몬스터가 기다리고 있어요!</p>
      </div>

      <CategoryGrid category={cat} problems={list} />
    </div>
  );
}
