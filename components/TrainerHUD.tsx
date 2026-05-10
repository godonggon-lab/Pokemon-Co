"use client";

// 헤더에 박히는 트레이너 HUD.
// 온보딩이 필요하면 이름 입력 모달을 띄운다.

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { useTrainer } from "./TrainerProvider";
import { badgeOf, nextBadge } from "@/lib/rating";
import { problems } from "@/lib/dataset";

export default function TrainerHUD() {
  const { profile, ready, needsOnboarding, createTrainer } = useTrainer();
  const [name, setName] = useState("");
  const pathname = usePathname();

  if (!ready) {
    return <div className="h-9 w-40 animate-pulse rounded-md bg-white/5" />;
  }

  if (needsOnboarding) {
    if (pathname === "/login") {
      return <div data-testid="guest-required" className="text-xs text-zinc-400">Guest 시작 전</div>;
    }

    return (
      <>
        <div className="text-xs text-zinc-400">트레이너 등록 필요</div>
        <Modal>
          <h2 className="text-lg font-bold">🎒 트레이너 등록</h2>
          <p className="mt-1 text-xs text-zinc-400">
            오박사: 너의 이름이... 뭐였더라?
          </p>
          <form
            className="mt-4 flex gap-2"
            onSubmit={async (e) => {
              e.preventDefault();
              if (!name.trim()) return;
              try {
                await createTrainer(name.trim());
              } catch (err: any) {
                alert(err?.message ?? "트레이너 생성 실패");
              }
            }}
          >
            <input
              autoFocus
              value={name}
              onChange={(e) => setName(e.target.value)}
              maxLength={16}
              placeholder="예: 한동준"
              className="flex-1 rounded-md border border-white/10 bg-zinc-900 px-3 py-2 text-sm outline-none focus:border-amber-400"
            />
            <button
              type="submit"
              disabled={!name.trim()}
              className="rounded-md bg-amber-500 px-3 py-2 text-sm font-bold text-zinc-900 disabled:opacity-50"
            >
              모험 시작
            </button>
          </form>
        </Modal>
      </>
    );
  }

  const p = profile!;
  const b = badgeOf(p.tr);
  const nb = nextBadge(p.tr);
  const pct = nb ? Math.min(100, ((p.tr - b.min) / (nb.min - b.min)) * 100) : 100;
  const dexN = Object.keys(p.captures).length;
  const dexPct = Math.round((dexN / Math.max(1, problems.length)) * 100);

  return (
    <Link href="/profile" className="flex items-center gap-3 rounded-lg border border-white/10 bg-zinc-900/60 px-3 py-1.5 hover:border-white/30">
      <span className={`flex h-8 w-8 items-center justify-center rounded-full text-base ring-2 ${b.ringClass} ${b.bgClass}`}>
        {b.emoji}
      </span>
      <div className="hidden text-left sm:block">
        <div className="flex items-baseline gap-2">
          <span className="text-sm font-bold">{p.name}</span>
          <span className={`text-[10px] font-semibold ${b.textClass}`}>{b.label}</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="font-mono text-xs text-amber-300">TR {p.tr}</span>
          <div className="h-1 w-20 overflow-hidden rounded-full bg-zinc-700">
            <div className="h-full bg-amber-400" style={{ width: `${pct}%` }} />
          </div>
          <span className="text-[10px] text-zinc-400">도감 {dexPct}%</span>
        </div>
      </div>
    </Link>
  );
}

function Modal({ children }: { children: React.ReactNode }) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
      <div className="w-[min(92vw,420px)] rounded-2xl border border-white/10 bg-zinc-900 p-6 shadow-2xl">
        {children}
      </div>
    </div>
  );
}
