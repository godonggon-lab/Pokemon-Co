"use client";

import Link from "next/link";
import Sprite from "@/components/Sprite";
import { useTrainer } from "@/components/TrainerProvider";
import { buildMonster, RARITY_BG, RARITY_LABEL, RARITY_RING } from "@/lib/characters";
import type { Category, Problem } from "@/lib/types";

export default function CategoryGrid({
  category,
  problems
}: {
  category: Category;
  problems: Problem[];
}) {
  const { profile } = useTrainer();
  const captured = profile?.captures ?? {};

  return (
    <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6">
      {problems.map((p, idx) => {
        const m = buildMonster(p);
        const isCaught = !!captured[p.slug];
        return (
          <Link
            key={p.slug}
            href={`/problem/${p.slug}`}
            className={`poke-card group relative flex flex-col items-center p-3 ${RARITY_RING[m.rarity]} ${RARITY_BG[m.rarity]}`}
            title={isCaught ? "포획 완료" : "미포획"}
            style={{ animationDelay: `${idx * 30}ms` }}
          >
            {isCaught && (
              <span className="absolute -right-1.5 -top-1.5 z-10 flex h-6 w-6 items-center justify-center rounded-full bg-emerald-500 text-xs shadow-md shadow-emerald-500/30">
                ✓
              </span>
            )}
            {m.rarity === "platinum" && (
              <span className="absolute left-2 top-2 animate-sparkle text-xs">★</span>
            )}
            <div className="text-[10px] text-white/30">No. {String(m.dexNo).padStart(4, "0")}</div>
            <div className="my-1 transition-transform group-hover:scale-110">
              <Sprite
                src={m.spriteUrl}
                alt={m.name}
                fallback={m.fallbackEmoji}
                size={88}
                silhouette={!isCaught}
              />
            </div>
            <div className="text-sm font-extrabold">
              {isCaught ? m.name : "???"}
            </div>
            <div className="mt-0.5 text-[10px] uppercase tracking-wider text-white/30">
              #{p.id} · {RARITY_LABEL[m.rarity]}
            </div>
          </Link>
        );
      })}
    </div>
  );
}
