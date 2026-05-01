"use client";

import { useEffect, useState } from "react";
import { useTrainer } from "@/components/TrainerProvider";
import { rivalLeaderboard } from "@/lib/rivals";
import { problems } from "@/lib/dataset";
import { badgeOf } from "@/lib/rating";

type RealUser = { id: number; name: string; tr: number; dexCount: number };

export default function LeaderboardPage() {
  const { profile, ready } = useTrainer();
  const total = problems.length;
  const rivals = rivalLeaderboard(total);
  const [real, setReal] = useState<RealUser[]>([]);

  useEffect(() => {
    fetch("/api/leaderboard?limit=100", { cache: "no-store" })
      .then(r => r.json())
      .then(j => setReal(j.trainers ?? []))
      .catch(() => {});
  }, [profile?.tr]);

  type Row = { id: string; name: string; emoji: string; tr: number; dexPct: number; isMe: boolean; isReal: boolean };
  const rows: Row[] = rivals.map((r) => ({ ...r, isMe: false, isReal: false }));
  for (const u of real) {
    const isMe = !!profile && u.name === profile.name;
    rows.push({
      id: `u-${u.id}`,
      name: u.name,
      emoji: isMe ? "🌟" : "🧑",
      tr: u.tr,
      dexPct: total ? u.dexCount / total : 0,
      isMe, isReal: true
    });
  }
  rows.sort((a, b) => b.tr - a.tr);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">🏆 명예의 전당</h1>
        <p className="text-sm text-zinc-400">전국 트레이너 랭킹 (TR 기준)</p>
      </div>

      <div className="overflow-hidden rounded-2xl border border-white/10">
        <table className="w-full text-sm">
          <thead className="bg-zinc-900 text-left text-xs uppercase tracking-wider text-zinc-400">
            <tr>
              <th className="px-4 py-3">순위</th>
              <th className="px-4 py-3">트레이너</th>
              <th className="px-4 py-3">배지</th>
              <th className="px-4 py-3 text-right">TR</th>
              <th className="px-4 py-3 text-right">도감</th>
              <th className="px-4 py-3">진행도</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r, i) => {
              const b = badgeOf(r.tr);
              const rank = i + 1;
              const medal = rank === 1 ? "🥇" : rank === 2 ? "🥈" : rank === 3 ? "🥉" : `#${rank}`;
              return (
                <tr
                  key={r.id}
                  className={`border-t border-white/5 ${r.isMe ? "bg-amber-500/10" : "hover:bg-white/5"}`}
                >
                  <td className="px-4 py-2 font-mono">{medal}</td>
                  <td className="px-4 py-2">
                    <span className="text-lg">{r.emoji}</span>{" "}
                    <span className={r.isMe ? "font-bold text-amber-300" : ""}>{r.name}</span>
                    {r.isMe && <span className="ml-2 text-[10px] text-amber-400">(나)</span>}
                    {r.isReal && !r.isMe && <span className="ml-2 text-[10px] text-emerald-400">실유저</span>}
                  </td>
                  <td className="px-4 py-2">
                    <span className={`pill ${b.bgClass} ${b.textClass} ring-1 ${b.ringClass}`}>
                      {b.emoji} {b.label}
                    </span>
                  </td>
                  <td className="px-4 py-2 text-right font-mono text-amber-300">{r.tr}</td>
                  <td className="px-4 py-2 text-right text-zinc-300">{(r.dexPct * 100).toFixed(1)}%</td>
                  <td className="px-4 py-2">
                    <div className="h-1.5 w-32 overflow-hidden rounded-full bg-zinc-800">
                      <div className="h-full bg-emerald-400" style={{ width: `${r.dexPct * 100}%` }} />
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      <p className="text-xs text-zinc-500">
        💡 라이벌은 시드 기반 가상 진행도이며, 실유저는 서버 SQLite에 저장된 실제 트레이너입니다.
      </p>
    </div>
  );
}
