"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { useTrainer } from "@/components/TrainerProvider";
import { categories, problems, getProblem } from "@/lib/dataset";
import { buildMonster } from "@/lib/characters";
import Sprite from "@/components/Sprite";
import { badgeOf, nextBadge, BADGES } from "@/lib/rating";

type LinkedAccount = {
  provider: "kakao" | "naver";
  providerUserId: string;
  email: string | null;
  displayName: string | null;
};

export default function ProfilePage() {
  const { profile, ready, resetTrainer, needsOnboarding } = useTrainer();
  const [accounts, setAccounts] = useState<LinkedAccount[]>([]);

  useEffect(() => {
    if (!profile) return;
    fetch("/api/auth/accounts", { cache: "no-store" })
      .then((r) => r.json())
      .then((j) => setAccounts(j.accounts ?? []))
      .catch(() => setAccounts([]));
  }, [profile]);

  if (!ready) return <div className="text-zinc-400">로딩 중...</div>;
  if (needsOnboarding || !profile) {
    return <div className="text-sm text-zinc-400">먼저 헤더에서 트레이너 등록을 해주세요.</div>;
  }

  const b = badgeOf(profile.tr);
  const nb = nextBadge(profile.tr);
  const dexN = Object.keys(profile.captures).length;
  const dexPct = (dexN / Math.max(1, problems.length)) * 100;

  // 카테고리별 진행도
  const perCat = categories.map((c) => {
    const total = problems.filter((p) => p.categorySlug === c.slug).length;
    const got = problems.filter(
      (p) => p.categorySlug === c.slug && profile.captures[p.slug]
    ).length;
    return { c, total, got };
  });

  // 최근 캡처
  const recentCaps = Object.values(profile.captures)
    .sort((a, b) => b.capturedAt - a.capturedAt)
    .slice(0, 12);

  return (
    <div className="space-y-8">
      <section className="rounded-3xl border border-white/10 bg-gradient-to-br from-zinc-900 to-zinc-950 p-6">
        <div className="flex flex-wrap items-center gap-6">
          <div className={`flex h-24 w-24 items-center justify-center rounded-full text-4xl ring-4 ${b.ringClass} ${b.bgClass}`}>
            {b.emoji}
          </div>
          <div className="flex-1">
            <div className="text-sm text-zinc-400">트레이너</div>
            <div className="text-3xl font-bold">{profile.name}</div>
            <div className={`mt-1 text-sm font-semibold ${b.textClass}`}>{b.label}</div>
          </div>
          <div className="grid grid-cols-2 gap-3 text-center sm:grid-cols-3">
            <Stat label="TR" value={profile.tr} accent="text-amber-300" />
            <Stat label="포획" value={`${dexN} / ${problems.length}`} />
            <Stat label="도감" value={`${dexPct.toFixed(1)}%`} />
          </div>
        </div>

        {nb && (
          <div className="mt-5">
            <div className="mb-1 flex justify-between text-xs text-zinc-400">
              <span>{b.label}</span>
              <span>다음: {nb.label} ({nb.min} TR)</span>
            </div>
            <div className="h-2 overflow-hidden rounded-full bg-zinc-800">
              <div
                className="h-full bg-gradient-to-r from-amber-400 to-rose-500"
                style={{ width: `${Math.min(100, ((profile.tr - b.min) / (nb.min - b.min)) * 100)}%` }}
              />
            </div>
          </div>
        )}
      </section>

      <section className="rounded-2xl border border-amber-400/20 bg-amber-400/5 p-4">
        <div className="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
          <div>
            <h2 className="text-lg font-bold text-amber-100">기록 보관</h2>
            <p className="mt-1 text-sm text-zinc-300">
              카카오나 네이버 계정을 연결하면 새 기기에서도 같은 트레이너 기록을 이어갈 수 있습니다.
            </p>
            {accounts.length > 0 && (
              <div className="mt-2 flex flex-wrap gap-2 text-xs">
                {accounts.map((a) => (
                  <span key={`${a.provider}:${a.providerUserId}`} className="rounded bg-emerald-500/15 px-2 py-1 text-emerald-200">
                    {a.provider === "kakao" ? "카카오" : "네이버"} 연결됨
                  </span>
                ))}
              </div>
            )}
          </div>
          <div className="flex flex-wrap gap-2">
            <Link
              href="/api/auth/kakao/start"
              className="rounded-md bg-[#FEE500] px-3 py-2 text-sm font-bold text-zinc-950 hover:brightness-95"
            >
              카카오로 기록 보관하기
            </Link>
            <Link
              href="/api/auth/naver/start"
              className="rounded-md bg-[#03C75A] px-3 py-2 text-sm font-bold text-white hover:brightness-110"
            >
              네이버로 기록 보관하기
            </Link>
          </div>
        </div>
      </section>

      <section>
        <h2 className="mb-3 text-lg font-bold">배지 진행도</h2>
        <div className="flex flex-wrap gap-2">
          {BADGES.map((badge) => {
            const owned = profile.tr >= badge.min;
            return (
              <div
                key={badge.id}
                className={`pill ${owned ? `${badge.bgClass} ${badge.textClass} ring-2 ${badge.ringClass}` : "bg-zinc-800/50 text-zinc-500"}`}
                title={`${badge.label} (${badge.min}+)`}
              >
                <span className={owned ? "" : "grayscale"}>{badge.emoji}</span>
                {badge.label}
              </div>
            );
          })}
        </div>
      </section>

      <section>
        <h2 className="mb-3 text-lg font-bold">분류별 도감 진행도</h2>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {perCat.map(({ c, total, got }) => {
            const pct = total > 0 ? (got / total) * 100 : 0;
            return (
              <Link key={c.slug} href={`/category/${c.slug}`} className="pixel-card p-4">
                <div className="flex items-baseline justify-between">
                  <div className="font-bold">{c.name_ko}</div>
                  <div className="text-xs text-zinc-400">{got} / {total}</div>
                </div>
                <div className="mt-2 h-1.5 overflow-hidden rounded-full bg-zinc-800">
                  <div className="h-full bg-emerald-400" style={{ width: `${pct}%` }} />
                </div>
              </Link>
            );
          })}
        </div>
      </section>

      <section>
        <h2 className="mb-3 text-lg font-bold">최근 포획 ({recentCaps.length})</h2>
        {recentCaps.length === 0 ? (
          <div className="rounded-xl border border-dashed border-white/15 p-6 text-center text-sm text-zinc-400">
            아직 포획한 몬스터가 없습니다.
          </div>
        ) : (
          <div className="grid grid-cols-3 gap-3 sm:grid-cols-4 md:grid-cols-6">
            {recentCaps.map((rec) => {
              const p = getProblem(rec.problemSlug);
              if (!p) return null;
              const m = buildMonster(p);
              return (
                <Link key={rec.problemSlug} href={`/problem/${p.slug}`} className="pixel-card p-3 text-center">
                  <Sprite src={m.spriteUrl} alt={m.name} fallback={m.fallbackEmoji} size={72} />
                  <div className="mt-1 text-xs font-bold">{m.name}</div>
                  <div className="text-[10px] text-zinc-500">No.{String(m.dexNo).padStart(4,"0")} · 시도 {rec.attempts}회</div>
                </Link>
              );
            })}
          </div>
        )}
      </section>

      <section>
        <h2 className="mb-3 text-lg font-bold">레이팅 변동 (최근 {profile.history.length})</h2>
        {profile.history.length === 0 ? (
          <div className="text-sm text-zinc-500">아직 기록이 없습니다.</div>
        ) : (
          <div className="overflow-hidden rounded-xl border border-white/10">
            <table className="w-full text-sm">
              <thead className="bg-zinc-900 text-left text-xs uppercase tracking-wider text-zinc-400">
                <tr>
                  <th className="px-3 py-2">결과</th>
                  <th className="px-3 py-2">상대 R</th>
                  <th className="px-3 py-2">기대값</th>
                  <th className="px-3 py-2">K</th>
                  <th className="px-3 py-2">변동</th>
                  <th className="px-3 py-2">→ TR</th>
                </tr>
              </thead>
              <tbody>
                {profile.history.slice(0, 20).map((h, i) => (
                  <tr key={i} className="border-t border-white/5">
                    <td className={`px-3 py-1.5 font-bold ${h.outcome === "win" ? "text-emerald-400" : "text-rose-400"}`}>
                      {h.outcome === "win" ? "AC" : "WA"}
                    </td>
                    <td className="px-3 py-1.5 font-mono">{h.problemR}</td>
                    <td className="px-3 py-1.5 font-mono">{h.expected.toFixed(2)}</td>
                    <td className="px-3 py-1.5 font-mono">{h.k}</td>
                    <td className={`px-3 py-1.5 font-mono ${h.delta >= 0 ? "text-emerald-300" : "text-rose-300"}`}>
                      {h.delta >= 0 ? "+" : ""}{h.delta}
                    </td>
                    <td className="px-3 py-1.5 font-mono">{h.nextTR}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <div className="pt-6 text-right">
        <button
          onClick={() => {
            if (confirm("정말 모든 기록을 초기화할까요?")) resetTrainer();
          }}
          className="text-xs text-rose-400 hover:underline"
        >
          ⚠ 트레이너 초기화
        </button>
      </div>
    </div>
  );
}

function Stat({ label, value, accent }: { label: string; value: string | number; accent?: string }) {
  return (
    <div className="rounded-xl border border-white/10 bg-zinc-900 px-4 py-2">
      <div className="text-[10px] uppercase tracking-wider text-zinc-500">{label}</div>
      <div className={`text-lg font-semibold ${accent ?? ""}`}>{value}</div>
    </div>
  );
}
