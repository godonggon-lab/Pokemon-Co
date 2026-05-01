"use client";

import Link from "next/link";
import { useTrainer } from "@/components/TrainerProvider";
import type { Problem, Category } from "@/lib/types";
import { buildMonster, RARITY_LABEL, RARITY_RING, RARITY_BG } from "@/lib/characters";
import Sprite from "@/components/Sprite";

export default function CategoryGrid({
  category, problems
}: { category: Category; problems: Problem[] }) {
  const { profile } = useTrainer();
  const captured = profile?.captures ?? {};

  return (
    <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6">
      {problems.map((p) => {
        const m = buildMonster(p);
        const isCaught = !!captured[p.slug];
        return (
          <Link
            key={p.slug}
            href={`/problem/${p.slug}`}
            className={`pixel-card relative flex flex-col items-center p-3 ${RARITY_RING[m.rarity]} ${RARITY_BG[m.rarity]}`}
            title={isCaught ? "포획 완료" : "미포획"}
          >
            {isCaught && (
              <span className="absolute -right-2 -top-2 z-10 flex h-6 w-6 items-center justify-center rounded-full bg-emerald-500 text-xs shadow">
                ✓
              </span>
            )}
            {m.rarity === "legendary" && (
              <span className="absolute left-2 top-2 text-xs">⚡</span>
            )}
            {m.rarity === "mythical" && (
              <span className="absolute left-2 top-2 text-xs">✨</span>
            )}
            <div className="text-[10px] text-zinc-400">No. {String(m.dexNo).padStart(4, "0")}</div>
            <div className="my-1">
              <Sprite
                src={m.spriteUrl}
                alt={m.name}
                fallback={m.fallbackEmoji}
                size={88}
                silhouette={!isCaught}
              />
            </div>
            <div className="text-sm font-bold">
              {isCaught ? m.name : "???"}
            </div>
            <div className="mt-0.5 text-[10px] uppercase tracking-wider text-zinc-400">
              #{p.id} · {RARITY_LABEL[m.rarity]}
            </div>
          </Link>
        );
      })}
    </div>
  );
}
