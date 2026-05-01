import Link from "next/link";
import { notFound } from "next/navigation";
import { getCategory, getProblem, problems } from "@/lib/dataset";
import { buildMonster, getMonsterEntry, RARITY_LABEL, RARITY_BG, RARITY_RING, POKE_TYPE_BG, POKE_TYPE_KO } from "@/lib/characters";
import { buildFlavor } from "@/lib/flavor";
import { getProblemMeta } from "@/lib/meta";
import ProblemPlayground from "@/components/ProblemPlayground";
import Sprite from "@/components/Sprite";
import FlavorBody from "@/components/FlavorBody";

export function generateStaticParams() {
  return problems.map((p) => ({ slug: p.slug }));
}

export default function ProblemPage({ params }: { params: { slug: string } }) {
  const problem = getProblem(params.slug);
  if (!problem) notFound();
  const cat = getCategory(problem.categorySlug)!;
  const m = buildMonster(problem);
  const monsterEntry = getMonsterEntry(problem.slug)!;
  const meta = getProblemMeta(problem.id);
  const flavor = buildFlavor(problem, monsterEntry, meta);

  return (
    <div className="space-y-6">
      <Link href={`/category/${cat.slug}`} className="text-xs text-zinc-400 hover:text-white">
        ← {cat.name_ko}
      </Link>

      <section className={`flex flex-wrap items-center gap-6 rounded-3xl border border-white/10 p-6 ${RARITY_BG[m.rarity]} ${RARITY_RING[m.rarity]}`}>
        <div className="rounded-2xl bg-black/20 p-2">
          <Sprite
            src={m.artworkUrl}
            alt={m.name}
            fallback={m.fallbackEmoji}
            size={160}
            pixelated={false}
          />
        </div>
        <div className="min-w-[240px] flex-1">
          <div className="text-xs text-zinc-400">
            전국도감 No. <b className="font-mono text-amber-300">{String(m.dexNo).padStart(4, "0")}</b>
            {" · "}{cat.name_ko}{" · "}{m.generation}세대
          </div>
          <h1 className="mt-1 text-3xl font-bold">
            {m.name} <span className="text-base font-normal text-zinc-400">({m.enName})</span>
          </h1>
          <div className="mt-2 flex flex-wrap items-center gap-2">
            <span className="pill bg-amber-500/20 text-amber-200 ring-1 ring-amber-400">
              {RARITY_LABEL[m.rarity]}
            </span>
            {m.types.map((t) => (
              <span key={t} className={`pill text-white ${POKE_TYPE_BG[t] ?? "bg-zinc-700"}`}>
                {POKE_TYPE_KO[t] ?? t}
              </span>
            ))}
            <span className="pill bg-white/10 text-zinc-300">BOJ #{problem.id}</span>
            {problem.link && (
              <a href={problem.link} target="_blank" rel="noreferrer"
                 className="text-xs text-amber-400 hover:underline">
                원본 ↗
              </a>
            )}
          </div>
          <div className="mt-3">
            <StatsBadge stats={m.baseStats} />
          </div>
        </div>
      </section>

      <section className="rounded-xl border border-white/10 bg-zinc-900/50 p-4 text-sm text-zinc-300">
        야생의 <b>{m.name}</b>이(가) 나타났다! 작성자: {problem.authors.length ? problem.authors.join(", ") : "익명"}.
      </section>

      <FlavorBody flavor={flavor} meta={meta} />

      <ProblemPlayground problem={problem} category={cat} />
    </div>
  );
}

function StatsBadge({ stats }: { stats: { hp:number; atk:number; def:number; spd:number } }) {
  const items: [string, number][] = [["HP", stats.hp], ["ATK", stats.atk], ["DEF", stats.def], ["SPD", stats.spd]];
  return (
    <div className="grid grid-cols-2 gap-1 text-[11px]">
      {items.map(([k, v]) => (
        <div key={k} className="flex items-center gap-2 rounded bg-white/5 px-2 py-1">
          <span className="w-7 text-zinc-400">{k}</span>
          <div className="h-1.5 w-24 overflow-hidden rounded bg-zinc-700">
            <div className="h-full bg-amber-400" style={{ width: `${Math.min(100, v)}%` }} />
          </div>
          <span className="w-6 text-right tabular-nums">{v}</span>
        </div>
      ))}
    </div>
  );
}
