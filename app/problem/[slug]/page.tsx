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
      <Link href={`/category/${cat.slug}`} className="inline-flex items-center gap-1 text-xs text-white/40 transition-colors hover:text-amber-300">
        ← {cat.name_ko}
      </Link>

      <section className={`poke-card flex flex-wrap items-center gap-6 p-6 ${RARITY_RING[m.rarity]} ${RARITY_BG[m.rarity]}`}>
        <div className="rounded-2xl bg-black/20 p-3">
          <Sprite
            src={m.artworkUrl}
            alt={m.name}
            fallback={m.fallbackEmoji}
            size={160}
            pixelated={false}
          />
        </div>
        <div className="min-w-[240px] flex-1">
          <div className="text-xs text-white/40">
            전국도감 No. <b className="font-mono text-amber-300">{String(m.dexNo).padStart(4, "0")}</b>
            {" · "}{cat.name_ko}{" · "}{m.generation}세대
          </div>
          <h1 className="mt-1 text-3xl font-extrabold">
            {m.name} <span className="text-base font-normal text-white/40">({m.enName})</span>
          </h1>
          <div className="mt-2 flex flex-wrap items-center gap-2">
            <span className="pill bg-amber-500/20 text-amber-300 ring-1 ring-amber-400/40">
              {RARITY_LABEL[m.rarity]}
            </span>
            {m.types.map((t) => (
              <span key={t} className={`pill text-white ${POKE_TYPE_BG[t] ?? "bg-zinc-700"}`}>
                {POKE_TYPE_KO[t] ?? t}
              </span>
            ))}
            <span className="pill bg-white/[0.06] text-white/50">#{problem.id}</span>
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

      <section className="poke-card p-4 text-sm text-white/60">
        <span className="text-lg">⚔️</span> 야생의 <b className="text-white/90">{m.name}</b>이(가) 나타났다!
        {problem.authors.length > 0 && <span className="text-white/30"> · 작성자: {problem.authors.join(", ")}</span>}
      </section>

      <FlavorBody flavor={flavor} meta={meta} />

      <ProblemPlayground problem={problem} category={cat} />
    </div>
  );
}

function StatsBadge({ stats }: { stats: { hp:number; atk:number; def:number; spd:number } }) {
  const items: [string, number, string][] = [
    ["HP", stats.hp, "from-emerald-400 to-emerald-300"],
    ["ATK", stats.atk, "from-rose-400 to-rose-300"],
    ["DEF", stats.def, "from-sky-400 to-sky-300"],
    ["SPD", stats.spd, "from-amber-400 to-amber-300"],
  ];
  return (
    <div className="grid grid-cols-2 gap-1.5 text-[11px]">
      {items.map(([k, v, gradient]) => (
        <div key={k} className="flex items-center gap-2 rounded-lg bg-white/[0.04] px-2.5 py-1.5">
          <span className="w-7 font-bold text-white/40">{k}</span>
          <div className="h-1.5 w-24 overflow-hidden rounded-full bg-white/[0.06]">
            <div className={`h-full rounded-full bg-gradient-to-r ${gradient}`} style={{ width: `${Math.min(100, v)}%` }} />
          </div>
          <span className="w-6 text-right font-bold tabular-nums text-white/60">{v}</span>
        </div>
      ))}
    </div>
  );
}
