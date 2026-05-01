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
        <Link href="/" className="text-xs text-zinc-400 hover:text-white">← 도감으로</Link>
        <h1 className="mt-2 text-3xl font-bold">
          {cat.name_ko} <span className="text-sm font-normal text-zinc-400">/ {cat.type}</span>
        </h1>
        <p className="text-sm text-zinc-400">총 {list.length} 마리</p>
      </div>

      <CategoryGrid category={cat} problems={list} />
    </div>
  );
}
