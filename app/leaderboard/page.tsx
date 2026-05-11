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
        <h1 className="section-title flex items-center gap-2">
          <span>🏆</span> 명예의 전당
        </h1>
        <p className="mt-1 text-sm text-white/40">트레이너 랭킹에서 나의 위치를 확인해보세요!</p>
      </div>

      {/* 상위 3명 하이라이트 */}
      {rows.length >= 3 && (
        <div className="grid grid-cols-3 gap-3">
          {[1, 0, 2].map((ri) => {
            const r = rows[ri];
            if (!r) return null;
            const b = badgeOf(r.tr);
            const medals = ["🥇", "🥈", "🥉"];
            const rank = ri + 1;
            const isCenter = ri === 0;
            return (
              <div
                key={r.id}
                className={`poke-card flex flex-col items-center px-4 py-5 text-center ${
                  isCenter ? "order-first sm:order-none scale-105 ring-1 ring-amber-400/20" : ""
                } ${r.isMe ? "ring-1 ring-amber-400/30" : ""}`}
              >
                <span className="text-3xl">{medals[ri]}</span>
                <span className="mt-2 text-2xl">{r.emoji}</span>
                <span className={`mt-1 text-sm font-extrabold ${r.isMe ? "text-amber-300" : ""}`}>
                  {r.name}
                </span>
                <span className={`mt-0.5 text-xs font-bold ${b.textClass}`}>{b.emoji} {b.label}</span>
                <span className="mt-1 font-mono text-lg font-bold text-amber-300">TR {r.tr}</span>
              </div>
            );
          })}
        </div>
      )}

      <div className="overflow-hidden rounded-2xl border border-white/[0.06]" style={{ background: "linear-gradient(145deg, #1e1f3b, #1a1b32)" }}>
        <table className="poke-table">
          <thead>
            <tr>
              <th>순위</th>
              <th>트레이너</th>
              <th>배지</th>
              <th className="text-right">TR</th>
              <th className="text-right">도감</th>
              <th>진행도</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((r, i) => {
              const b = badgeOf(r.tr);
              const rank = i + 1;
              const medal = rank === 1 ? "🥇" : rank === 2 ? "🥈" : rank === 3 ? "🥉" : `${rank}`;
              return (
                <tr
                  key={r.id}
                  className={r.isMe ? "!bg-amber-500/[0.06]" : ""}
                >
                  <td className="font-mono text-white/50">{medal}</td>
                  <td>
                    <span className="text-lg">{r.emoji}</span>{" "}
                    <span className={r.isMe ? "font-extrabold text-amber-300" : "font-semibold"}>{r.name}</span>
                    {r.isMe && <span className="ml-2 rounded-full bg-amber-500/10 px-2 py-0.5 text-[10px] font-bold text-amber-300">나</span>}
                    {r.isReal && !r.isMe && <span className="ml-2 rounded-full bg-emerald-500/10 px-2 py-0.5 text-[10px] font-bold text-emerald-300">실제</span>}
                  </td>
                  <td>
                    <span className={`pill ${b.bgClass} ${b.textClass} ring-1 ${b.ringClass}`}>
                      {b.emoji} {b.label}
                    </span>
                  </td>
                  <td className="text-right font-mono font-bold text-amber-300">{r.tr}</td>
                  <td className="text-right text-white/50">{(r.dexPct * 100).toFixed(1)}%</td>
                  <td>
                    <div className="h-2 w-32 overflow-hidden rounded-full bg-white/[0.06]">
                      <div
                        className="h-full rounded-full bg-gradient-to-r from-emerald-400 to-emerald-300 transition-all"
                        style={{ width: `${r.dexPct * 100}%` }}
                      />
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      <p className="flex items-center gap-1 text-xs text-white/25">
        <span>💡</span> 라이벌 트레이너들과 함께 경쟁해보세요!
      </p>
    </div>
  );
}
