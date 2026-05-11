"use client";

import Link from "next/link";
import { useTrainer } from "./TrainerProvider";
import { badgeOf, nextBadge } from "@/lib/rating";
import { problems } from "@/lib/dataset";

export default function TrainerHUD() {
  const { profile, ready, needsOnboarding } = useTrainer();

  if (!ready) {
    return <div className="h-9 w-40 animate-pulse rounded-xl bg-white/5" />;
  }

  if (needsOnboarding || !profile) {
    return (
      <Link
        data-testid="login-entry"
        href="/login"
        className="btn-primary !px-4 !py-2 text-xs"
      >
        시작하기 ⚡
      </Link>
    );
  }

  const b = badgeOf(profile.tr);
  const nb = nextBadge(profile.tr);
  const pct = nb ? Math.min(100, ((profile.tr - b.min) / (nb.min - b.min)) * 100) : 100;
  const dexN = Object.keys(profile.captures).length;
  const dexPct = Math.round((dexN / Math.max(1, problems.length)) * 100);

  return (
    <Link href="/profile" className="group flex items-center gap-3 rounded-xl border border-white/[0.06] bg-white/[0.03] px-3 py-1.5 transition-all hover:bg-white/[0.06]">
      <span className={`flex h-8 w-8 items-center justify-center rounded-lg text-base ring-2 ${b.ringClass} ${b.bgClass} transition-transform group-hover:scale-110`}>
        {b.emoji}
      </span>
      <div className="hidden text-left sm:block">
        <div className="flex items-baseline gap-2">
          <span className="text-sm font-extrabold">{profile.name}</span>
          <span className={`text-[10px] font-bold ${b.textClass}`}>{b.label}</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="font-mono text-xs font-bold text-amber-300">TR {profile.tr}</span>
          <div className="h-1.5 w-16 overflow-hidden rounded-full bg-white/[0.08]">
            <div className="h-full rounded-full bg-gradient-to-r from-amber-400 to-orange-400" style={{ width: `${pct}%` }} />
          </div>
          <span className="text-[10px] text-white/30">📖 {dexPct}%</span>
        </div>
      </div>
    </Link>
  );
}
