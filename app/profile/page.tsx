"use client";

import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { Suspense, useEffect, useState } from "react";
import { useTrainer } from "@/components/TrainerProvider";
import { categories, getProblem, problems } from "@/lib/dataset";
import { buildMonster } from "@/lib/characters";
import Sprite from "@/components/Sprite";
import { BADGES, badgeOf, nextBadge } from "@/lib/rating";

type LinkedAccount = {
  provider: "kakao" | "naver";
  providerUserId: string;
  email: string | null;
  displayName: string | null;
};

export default function ProfilePage() {
  return (
    <Suspense fallback={<div className="text-white/40">로딩 중...</div>}>
      <ProfileContent />
    </Suspense>
  );
}

function ProfileContent() {
  const router = useRouter();
  const { profile, ready, refreshTrainer, resetTrainer, needsOnboarding } = useTrainer();
  const [accounts, setAccounts] = useState<LinkedAccount[]>([]);
  const [showAuthPrompt, setShowAuthPrompt] = useState(false);
  const searchParams = useSearchParams();
  const authSignal = searchParams.toString();
  const accountLinked = accounts.length > 0;

  useEffect(() => {
    if (authSignal) {
      refreshTrainer().catch(() => {});
    }
  }, [authSignal, refreshTrainer]);

  useEffect(() => {
    if (!profile) return;
    fetch("/api/auth/accounts", { cache: "no-store" })
      .then((r) => r.json())
      .then((j) => setAccounts(j.accounts ?? []))
      .catch(() => setAccounts([]));
  }, [profile, authSignal]);

  useEffect(() => {
    if (accountLinked) setShowAuthPrompt(false);
  }, [accountLinked]);

  async function logout() {
    await resetTrainer();
    router.push("/login");
  }

  if (!ready) return <div className="text-white/40">로딩 중...</div>;
  if (needsOnboarding || !profile) {
    return (
      <div className="poke-card p-8 text-center">
        <span className="text-5xl">🎮</span>
        <h2 className="mt-4 text-xl font-extrabold">아직 트레이너가 없어요</h2>
        <p className="mt-2 text-sm text-white/50">먼저 트레이너를 만들고 모험을 시작해보세요!</p>
        <div className="mt-6">
          <Link href="/login" className="btn-primary">
            시작하기 ⚡
          </Link>
        </div>
      </div>
    );
  }

  const b = badgeOf(profile.tr);
  const nb = nextBadge(profile.tr);
  const dexN = Object.keys(profile.captures).length;
  const dexPct = (dexN / Math.max(1, problems.length)) * 100;
  const perCat = categories.map((c) => {
    const total = problems.filter((p) => p.categorySlug === c.slug).length;
    const got = problems.filter((p) => p.categorySlug === c.slug && profile.captures[p.slug]).length;
    return { c, total, got };
  });
  const recentCaps = Object.values(profile.captures)
    .sort((a, b) => b.capturedAt - a.capturedAt)
    .slice(0, 12);

  return (
    <div className="space-y-8">
      {/* 트레이너 프로필 카드 */}
      <section className="poke-card overflow-hidden">
        <div className="bg-gradient-to-r from-amber-500/5 to-rose-500/5 p-6">
          <div className="flex flex-wrap items-center gap-6">
            <div className={`flex h-24 w-24 items-center justify-center rounded-2xl text-4xl ring-4 ${b.ringClass} ${b.bgClass} shadow-lg`}>
              {b.emoji}
            </div>
            <div className="flex-1">
              <div className="text-xs font-bold uppercase text-white/30">트레이너</div>
              <div className="text-3xl font-extrabold">{profile.name}</div>
              <div className={`mt-1 text-sm font-bold ${b.textClass}`}>{b.label}</div>
            </div>
            <div className="grid grid-cols-2 gap-3 text-center sm:grid-cols-3">
              <Stat emoji="⚡" label="TR" value={profile.tr} accent="text-amber-300" />
              <Stat emoji="🎯" label="포획" value={`${dexN} / ${problems.length}`} />
              <Stat emoji="📊" label="도감" value={`${dexPct.toFixed(1)}%`} />
            </div>
          </div>

          {nb && (
            <div className="mt-5">
              <div className="mb-1.5 flex justify-between text-xs text-white/40">
                <span>{b.emoji} {b.label}</span>
                <span>다음: {nb.label} ({nb.min} TR)</span>
              </div>
              <div className="h-2.5 overflow-hidden rounded-full bg-white/[0.06]">
                <div
                  className="h-full rounded-full bg-gradient-to-r from-amber-400 to-rose-500 transition-all"
                  style={{ width: `${Math.min(100, ((profile.tr - b.min) / (nb.min - b.min)) * 100)}%` }}
                />
              </div>
            </div>
          )}
        </div>
      </section>

      {/* 계정 연결 */}
      <section className={`poke-card p-5 ${accountLinked ? "ring-1 ring-emerald-400/20" : "ring-1 ring-amber-400/20"}`}>
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <div className="flex flex-wrap items-center gap-2">
              <h2 className="text-lg font-extrabold">
                {accountLinked ? "✅ 계정 연결됨" : "💾 계정 연결"}
              </h2>
              {accountLinked ? (
                <span data-testid="auth-status" className="rounded-full bg-emerald-500/15 px-2.5 py-0.5 text-xs font-bold text-emerald-300">
                  로그인됨
                </span>
              ) : (
                <span data-testid="guest-status" className="rounded-full bg-amber-500/15 px-2.5 py-0.5 text-xs font-bold text-amber-300">
                  체험 중
                </span>
              )}
            </div>
            <p className="mt-1 max-w-2xl text-sm leading-6 text-white/50">
              {accountLinked
                ? "소셜 계정에 연결되어 있어요. 어디서든 같은 프로필로 이어할 수 있어요!"
                : "카카오로 연결하면 기록이 안전하게 저장되고, 다른 기기에서도 이어할 수 있어요."}
            </p>
            {accountLinked && (
              <div data-testid="linked-accounts" className="mt-3 flex flex-wrap gap-2 text-xs">
                {accounts.map((a) => (
                  <span key={`${a.provider}:${a.providerUserId}`} className="flex items-center gap-1 rounded-full bg-emerald-500/10 px-3 py-1 text-emerald-300">
                    ✅ {a.provider === "kakao" ? "카카오" : "네이버"} 연결됨
                    {a.displayName ? ` · ${a.displayName}` : ""}
                  </span>
                ))}
              </div>
            )}
          </div>
          <div className="flex flex-wrap gap-2">
            {accountLinked ? (
              <Link
                data-testid="protected-profile-link"
                href="/profile"
                className="inline-flex items-center gap-1 rounded-xl bg-emerald-500/10 px-4 py-2.5 text-sm font-bold text-emerald-300"
              >
                🔒 보호된 프로필
              </Link>
            ) : (
              <button
                data-testid="save-records-cta"
                onClick={() => setShowAuthPrompt(true)}
                className="btn-primary"
              >
                카카오로 연결하기
              </button>
            )}
            <button
              data-testid="logout-button"
              onClick={logout}
              className="btn-secondary"
            >
              로그아웃
            </button>
          </div>
        </div>
      </section>

      {showAuthPrompt && !accountLinked && (
        <div data-testid="auth-required-modal" className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" style={{ backdropFilter: "blur(4px)" }}>
          <div className="w-[min(92vw,420px)] animate-slide-up poke-card p-6">
            <h2 className="flex items-center gap-2 text-lg font-extrabold">
              <span>💾</span> 카카오 계정으로 이어가기
            </h2>
            <p className="mt-2 text-sm leading-6 text-white/50">
              이미 연결된 계정이 있으면 그 프로필을 불러와요. 처음 연결하면 지금까지의 기록이 저장돼요!
            </p>
            <div className="mt-5 flex flex-col gap-2">
              <Link
                data-testid="kakao-login"
                href="/api/auth/kakao/start"
                className="flex items-center justify-center gap-2 rounded-xl bg-[#FEE500] px-4 py-3 text-center text-sm font-bold text-zinc-900 shadow-md transition-all hover:-translate-y-0.5"
              >
                카카오로 로그인
              </Link>
              <button
                data-testid="auth-modal-close"
                onClick={() => setShowAuthPrompt(false)}
                className="btn-secondary"
              >
                나중에 하기
              </button>
            </div>
          </div>
        </div>
      )}

      <section>
        <h2 className="section-title mb-3 flex items-center gap-2">
          <span>🏅</span> 배지 진행도
        </h2>
        <div className="flex flex-wrap gap-2">
          {BADGES.map((badge) => {
            const owned = profile.tr >= badge.min;
            return (
              <div
                key={badge.id}
                className={`pill ${owned ? `${badge.bgClass} ${badge.textClass} ring-2 ${badge.ringClass}` : "bg-white/[0.04] text-white/30"}`}
                title={`${badge.label} (${badge.min}+)`}
              >
                <span className={owned ? "" : "grayscale opacity-50"}>{badge.emoji}</span>
                {badge.label}
              </div>
            );
          })}
        </div>
      </section>

      <section>
        <h2 className="section-title mb-3 flex items-center gap-2">
          <span>📖</span> 분류별 도감
        </h2>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {perCat.map(({ c, total, got }) => {
            const pct = total > 0 ? (got / total) * 100 : 0;
            return (
              <Link key={c.slug} href={`/category/${c.slug}`} className="poke-card group p-4">
                <div className="flex items-baseline justify-between">
                  <div className="font-extrabold group-hover:text-amber-300 transition-colors">{c.name_ko}</div>
                  <div className="text-xs text-white/40">{got} / {total}</div>
                </div>
                <div className="mt-2 h-2 overflow-hidden rounded-full bg-white/[0.06]">
                  <div className="h-full rounded-full bg-gradient-to-r from-emerald-400 to-emerald-300 transition-all" style={{ width: `${pct}%` }} />
                </div>
              </Link>
            );
          })}
        </div>
      </section>

      <section>
        <h2 className="section-title mb-3 flex items-center gap-2">
          <span>🎯</span> 최근 포획 <span className="text-sm font-normal text-white/30">({recentCaps.length})</span>
        </h2>
        {recentCaps.length === 0 ? (
          <div className="poke-card p-8 text-center">
            <span className="text-4xl">🔍</span>
            <p className="mt-2 text-sm text-white/40">아직 포획한 몬스터가 없어요. 첫 도전을 시작해보세요!</p>
          </div>
        ) : (
          <div className="grid grid-cols-3 gap-3 sm:grid-cols-4 md:grid-cols-6">
            {recentCaps.map((rec) => {
              const p = getProblem(rec.problemSlug);
              if (!p) return null;
              const m = buildMonster(p);
              return (
                <Link key={rec.problemSlug} href={`/problem/${p.slug}`} className="poke-card group p-3 text-center">
                  <div className="transition-transform group-hover:scale-110">
                    <Sprite src={m.spriteUrl} alt={m.name} fallback={m.fallbackEmoji} size={72} />
                  </div>
                  <div className="mt-1 text-xs font-extrabold">{m.name}</div>
                  <div className="text-[10px] text-white/30">시도 {rec.attempts}회</div>
                </Link>
              );
            })}
          </div>
        )}
      </section>

      <section>
        <h2 className="section-title mb-3 flex items-center gap-2">
          <span>📝</span> 최근 제출 <span className="text-sm font-normal text-white/30">({profile.submissions.length})</span>
        </h2>
        {profile.submissions.length === 0 ? (
          <div className="poke-card p-8 text-center">
            <span className="text-4xl">📝</span>
            <p className="mt-2 text-sm text-white/40">아직 제출 기록이 없어요.</p>
          </div>
        ) : (
          <div className="overflow-x-auto rounded-2xl border border-white/[0.06]" style={{ background: "linear-gradient(145deg, #1e1f3b, #1a1b32)" }}>
            <table className="poke-table min-w-[760px]">
              <thead>
                <tr>
                  <th>문제</th>
                  <th>언어</th>
                  <th>결과</th>
                  <th>통과</th>
                  <th>실패</th>
                  <th>시간</th>
                  <th>제출</th>
                </tr>
              </thead>
              <tbody>
                {profile.submissions.slice(0, 20).map((s) => {
                  const p = getProblem(s.problemSlug);
                  return (
                    <tr key={s.id}>
                      <td>
                        {p ? (
                          <Link href={`/problem/${p.slug}`} className="font-semibold hover:text-amber-300 transition-colors">
                            #{p.id}
                          </Link>
                        ) : (
                          <span className="font-mono text-xs text-white/30">{s.problemSlug}</span>
                        )}
                      </td>
                      <td className="font-mono text-xs text-white/50">{s.lang}</td>
                      <td>
                        <span className={`rounded-full px-2.5 py-0.5 text-xs font-bold ${statusClass(s.status)}`}>
                          {s.status}
                        </span>
                      </td>
                      <td className="font-mono text-xs text-white/50">
                        {s.passed == null || s.total == null ? "-" : `${s.passed}/${s.total}`}
                      </td>
                      <td className="text-xs text-white/40">
                        {s.failedCaseKind ? `${s.failedCaseKind}${s.failedCaseVerdict ? `:${s.failedCaseVerdict}` : ""}` : "-"}
                      </td>
                      <td className="font-mono text-xs text-white/50">
                        {s.durationMs == null ? "-" : `${s.durationMs}ms`}
                      </td>
                      <td className="text-xs text-white/30">{formatWhen(s.ts)}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <section>
        <h2 className="section-title mb-3 flex items-center gap-2">
          <span>📈</span> 레이팅 변화 <span className="text-sm font-normal text-white/30">({profile.history.length})</span>
        </h2>
        {profile.history.length === 0 ? (
          <div className="text-sm text-white/30">아직 기록이 없어요.</div>
        ) : (
          <div className="overflow-hidden rounded-2xl border border-white/[0.06]" style={{ background: "linear-gradient(145deg, #1e1f3b, #1a1b32)" }}>
            <table className="poke-table">
              <thead>
                <tr>
                  <th>결과</th>
                  <th>상대 R</th>
                  <th>기대값</th>
                  <th>K</th>
                  <th>변화</th>
                  <th>새 TR</th>
                </tr>
              </thead>
              <tbody>
                {profile.history.slice(0, 20).map((h, i) => (
                  <tr key={i}>
                    <td className={`font-bold ${h.outcome === "win" ? "text-emerald-400" : "text-rose-400"}`}>
                      {h.outcome === "win" ? "✅ AC" : "❌ WA"}
                    </td>
                    <td className="font-mono text-white/50">{h.problemR}</td>
                    <td className="font-mono text-white/50">{h.expected.toFixed(2)}</td>
                    <td className="font-mono text-white/50">{h.k}</td>
                    <td className={`font-mono font-bold ${h.delta >= 0 ? "text-emerald-300" : "text-rose-300"}`}>
                      {h.delta >= 0 ? "+" : ""}{h.delta}
                    </td>
                    <td className="font-mono font-bold text-amber-300">{h.nextTR}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </div>
  );
}

function Stat({ emoji, label, value, accent }: { emoji: string; label: string; value: string | number; accent?: string }) {
  return (
    <div className="rounded-xl border border-white/[0.06] bg-white/[0.03] px-4 py-2.5">
      <div className="text-[10px] font-semibold uppercase text-white/30">{emoji} {label}</div>
      <div className={`text-lg font-extrabold ${accent ?? ""}`}>{value}</div>
    </div>
  );
}

function statusClass(status: string) {
  if (status === "AC") return "bg-emerald-500/15 text-emerald-200";
  if (status === "WA" || status === "PE") return "bg-rose-500/15 text-rose-200";
  if (status === "TLE" || status === "MLE" || status === "OLE") return "bg-amber-500/15 text-amber-200";
  if (status === "CE" || status === "RE" || status === "ERR") return "bg-zinc-700 text-zinc-200";
  return "bg-zinc-800 text-zinc-300";
}

function formatWhen(ts: number) {
  return new Intl.DateTimeFormat("ko-KR", {
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  }).format(new Date(ts));
}
