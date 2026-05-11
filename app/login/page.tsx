"use client";

import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { Suspense, useEffect, useState } from "react";
import { useTrainer } from "@/components/TrainerProvider";

type LinkedAccount = {
  provider: "kakao" | "naver";
  providerUserId: string;
  email: string | null;
  displayName: string | null;
};

/* 좌측 히어로에 떠다니는 포켓몬 */
const FLOATING_SPRITES = [
  { id: 25,  x: "12%", y: "22%", delay: "0s",   size: 80 },
  { id: 133, x: "72%", y: "15%", delay: "0.6s", size: 68 },
  { id: 39,  x: "20%", y: "70%", delay: "1.2s", size: 60 },
  { id: 4,   x: "75%", y: "65%", delay: "0.3s", size: 64 },
  { id: 7,   x: "50%", y: "42%", delay: "0.9s", size: 72 },
];

const FEATURES = [
  { emoji: "📖", title: "22개 알고리즘 분류", desc: "포켓몬 타입별로 분류된 알고리즘" },
  { emoji: "⚔️", title: "자동 채점 시스템", desc: "코드를 제출하면 즉시 결과 확인" },
  { emoji: "📊", title: "트레이너 레이팅", desc: "문제를 풀수록 성장하는 실력 지표" },
  { emoji: "🏆", title: "랭킹 경쟁", desc: "다른 트레이너들과 순위 경쟁" },
];

export default function LoginPage() {
  return (
    <Suspense fallback={<div className="text-sm text-white/40">로딩 중...</div>}>
      <LoginContent />
    </Suspense>
  );
}

function LoginContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { profile, ready, createTrainer, refreshTrainer, resetTrainer } = useTrainer();
  const [accounts, setAccounts] = useState<LinkedAccount[]>([]);
  const [accountsReady, setAccountsReady] = useState(false);
  const [guestFormOpen, setGuestFormOpen] = useState(false);
  const [name, setName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const needsSocialSignup = searchParams.get("auth") === "signup_required";
  const authError = searchParams.get("auth_error");
  const accountLinked = accounts.length > 0;

  useEffect(() => {
    if (!profile) {
      setAccounts([]);
      setAccountsReady(true);
      return;
    }
    setAccountsReady(false);
    fetch("/api/auth/accounts", { cache: "no-store" })
      .then((r) => r.json())
      .then((j) => setAccounts(j.accounts ?? []))
      .catch(() => setAccounts([]))
      .finally(() => setAccountsReady(true));
  }, [profile]);

  async function startGuest(e: React.FormEvent) {
    e.preventDefault();
    if (!name.trim()) return;
    setBusy(true);
    setError(null);
    try {
      await createTrainer(name.trim());
      router.push("/");
    } catch (err: any) {
      setError(err?.message ?? "세션 생성에 실패했어요");
    } finally {
      setBusy(false);
    }
  }

  async function logout() {
    await resetTrainer();
    setAccounts([]);
    setAccountsReady(true);
    router.push("/login");
  }

  async function completeSocialSignup(e: React.FormEvent) {
    e.preventDefault();
    if (!name.trim()) return;
    setBusy(true);
    setError(null);
    try {
      const res = await fetch("/api/auth/complete", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ name: name.trim() })
      });
      const body = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(body?.error ?? "가입에 실패했어요");
      await refreshTrainer();
      router.push(`/profile?auth=${body.mode === "signed_in" ? "signed_in" : "linked"}`);
    } catch (err: any) {
      setError(err?.message ?? "가입에 실패했어요");
    } finally {
      setBusy(false);
    }
  }

  /* 로딩 */
  if (!ready || (profile && !accountsReady)) {
    return (
      <div className="flex min-h-[60vh] items-center justify-center">
        <div className="animate-bounce-soft">
          <PokeBallSVG size={64} />
        </div>
      </div>
    );
  }

  /* 카카오 가입 완료 단계 */
  if (needsSocialSignup) {
    return (
      <SplitLayout
        formContent={
          <div className="flex flex-col gap-5">
            <div>
              <p className="text-xs font-bold uppercase tracking-wider text-emerald-400">카카오 인증 완료</p>
              <h1 className="mt-2 text-2xl font-extrabold tracking-tight">트레이너 이름을 정해주세요</h1>
              <p className="mt-2 text-sm text-white/50">
                앞으로 랭킹과 프로필에 표시될 이름이에요.
              </p>
            </div>
            <NameForm
              value={name}
              busy={busy}
              error={error}
              submitLabel="시작하기"
              busyLabel="프로필 생성 중..."
              onChange={setName}
              onSubmit={completeSocialSignup}
            />
          </div>
        }
      />
    );
  }

  /* 로그인됨 + 계정 연결됨 */
  if (profile && accountLinked) {
    return (
      <SplitLayout
        formContent={
          <div className="flex flex-col gap-5">
            <div>
              <p className="text-xs font-bold uppercase tracking-wider text-emerald-400">로그인됨</p>
              <h1 className="mt-2 text-2xl font-extrabold tracking-tight">
                {profile.name} 트레이너, 돌아왔군요!
              </h1>
            </div>
            <div data-testid="login-authenticated-session" className="flex items-center gap-3 rounded-xl bg-emerald-500/10 px-4 py-3 text-sm text-emerald-300">
              <span className="text-lg">✅</span>
              <span>카카오 계정에 연결된 프로필이에요.</span>
            </div>
            <div data-testid="login-current-session" className="text-sm text-white/50">
              현재 트레이너: <b className="text-amber-300">{profile.name}</b>
            </div>
            <div className="flex flex-col gap-2">
              <Link href="/" className="btn-primary text-center">도감으로 이동</Link>
              <div className="flex gap-2">
                <Link href="/profile" className="btn-secondary flex-1 text-center">프로필</Link>
                <button data-testid="login-logout" onClick={logout} className="btn-secondary flex-1">로그아웃</button>
              </div>
            </div>
          </div>
        }
      />
    );
  }

  /* 게스트 세션 */
  if (profile && !accountLinked) {
    return (
      <SplitLayout
        formContent={
          <div className="flex flex-col gap-5">
            <div>
              <p className="text-xs font-bold uppercase tracking-wider text-amber-400">체험 중</p>
              <h1 className="mt-2 text-2xl font-extrabold tracking-tight">
                기록을 안전하게 저장하세요
              </h1>
              <p className="mt-2 text-sm text-white/50">
                카카오 계정을 연결하면 어디서든 이어할 수 있어요.
              </p>
            </div>
            <div data-testid="login-guest-session" className="flex items-center gap-3 rounded-xl bg-amber-500/8 px-4 py-3 text-sm text-amber-300/80">
              <span className="text-lg">💡</span>
              <span>지금은 이 브라우저에만 기록이 저장되어 있어요.</span>
            </div>
            <div data-testid="login-current-session" className="text-sm text-white/50">
              현재 트레이너: <b className="text-amber-300">{profile.name}</b>
            </div>
            <div className="flex flex-col gap-2">
              <Link
                data-testid="login-kakao-start"
                href="/api/auth/kakao/start"
                className="flex items-center justify-center gap-2 rounded-xl bg-[#FEE500] px-5 py-3.5 text-sm font-bold text-zinc-900 shadow-md transition-all hover:-translate-y-0.5 hover:shadow-lg"
              >
                <KakaoIcon /> 카카오 계정 연결하기
              </Link>
              <div className="flex gap-2">
                <Link href="/" className="btn-secondary flex-1 text-center">계속 체험하기</Link>
                <button data-testid="login-logout" onClick={logout} className="btn-secondary flex-1">나가기</button>
              </div>
            </div>
          </div>
        }
      />
    );
  }

  /* 미로그인 — 기본 로그인 화면 */
  return (
    <SplitLayout
      formContent={
        <div className="flex flex-col gap-5">
          <div>
            <h1 className="text-2xl font-extrabold tracking-tight">
              시작하기
            </h1>
            <p className="mt-2 text-sm text-white/50">
              카카오 계정으로 로그인하거나, 먼저 체험해보세요.
            </p>
          </div>

          {authError && (
            <div data-testid="auth-error" className="flex items-center gap-2 rounded-xl bg-rose-500/10 px-4 py-3 text-sm text-rose-300">
              <span>😢</span> 로그인에 실패했어요. 다시 시도해 주세요.
            </div>
          )}

          <div className="flex flex-col gap-3">
            <Link
              data-testid="login-kakao-start"
              href="/api/auth/kakao/start"
              className="flex items-center justify-center gap-2 rounded-xl bg-[#FEE500] px-5 py-3.5 text-sm font-bold text-zinc-900 shadow-md transition-all hover:-translate-y-0.5 hover:shadow-lg"
            >
              <KakaoIcon /> 카카오로 시작하기
            </Link>

            <div className="flex items-center gap-3">
              <div className="h-px flex-1 bg-white/[0.06]" />
              <span className="text-xs text-white/20">또는</span>
              <div className="h-px flex-1 bg-white/[0.06]" />
            </div>

            <button
              data-testid="guest-start"
              onClick={() => { setGuestFormOpen(true); setError(null); }}
              className="btn-secondary"
            >
              체험 모드로 둘러보기
            </button>
          </div>

          {guestFormOpen && (
            <div data-testid="guest-name-panel" className="animate-fade-in rounded-xl border border-white/[0.06] bg-white/[0.02] p-4">
              <p className="text-sm font-bold">트레이너 이름을 정해주세요</p>
              <p className="mt-1 text-xs text-white/30">나중에 카카오 계정에 연결할 수 있어요.</p>
              <NameForm
                value={name}
                busy={busy}
                error={error}
                submitLabel="시작하기"
                busyLabel="준비 중..."
                onChange={setName}
                onSubmit={startGuest}
              />
            </div>
          )}

          <p data-testid="guest-login-hint" className="text-xs text-white/20">
            체험 기록은 프로필에서 카카오 계정에 연결할 수 있어요.
          </p>
        </div>
      }
    />
  );
}

/* ─── SaaS 스타일 좌우 분할 레이아웃 ─── */
function SplitLayout({ formContent }: { formContent: React.ReactNode }) {
  return (
    <div className="relative -mx-4 -mt-8 flex min-h-[calc(100vh-80px)] overflow-hidden">
      {/* 좌측: 가치 제안 + 포켓몬 일러스트 */}
      <div className="relative hidden w-[55%] flex-col justify-between overflow-hidden lg:flex"
           style={{ background: "linear-gradient(160deg, #1a1040 0%, #0f1a3a 50%, #0c1628 100%)" }}>

        {/* 장식 원 */}
        <div className="pointer-events-none absolute inset-0">
          <div className="absolute -left-32 -top-32 h-[500px] w-[500px] rounded-full"
               style={{ background: "radial-gradient(circle, rgba(245,158,11,0.08), transparent 70%)" }} />
          <div className="absolute -bottom-40 -right-40 h-[400px] w-[400px] rounded-full"
               style={{ background: "radial-gradient(circle, rgba(248,88,136,0.06), transparent 70%)" }} />
        </div>

        {/* 떠다니는 포켓몬 */}
        {FLOATING_SPRITES.map((s) => (
          <div
            key={s.id}
            className="pointer-events-none absolute"
            style={{ left: s.x, top: s.y, animationDelay: s.delay }}
          >
            <div className="animate-float opacity-20" style={{ animationDelay: s.delay }}>
              <img
                src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${s.id}.png`}
                alt=""
                width={s.size}
                height={s.size}
                className="drop-shadow-2xl"
                loading="lazy"
                onError={(e) => { (e.target as HTMLImageElement).style.display = "none"; }}
              />
            </div>
          </div>
        ))}

        {/* 텍스트 콘텐츠 */}
        <div className="relative z-10 flex flex-1 flex-col justify-center px-12 py-16 xl:px-16">
          <div className="flex items-center gap-3">
            <PokeBallSVG size={36} />
            <span className="text-xl font-extrabold">
              <span className="bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent">CodeDex</span>
            </span>
          </div>
          <h2 className="mt-8 text-3xl font-extrabold leading-tight tracking-tight xl:text-4xl">
            알고리즘을 잡아서<br />
            <span className="bg-gradient-to-r from-amber-300 via-orange-400 to-rose-400 bg-clip-text text-transparent">
              실력을 키우세요
            </span>
          </h2>
          <p className="mt-4 max-w-md text-sm leading-relaxed text-white/40">
            포켓몬 도감 컨셉으로 알고리즘 문제를 풀고, 트레이너 레이팅으로 성장을 추적하세요.
          </p>

          <div className="mt-10 grid grid-cols-2 gap-4">
            {FEATURES.map((f) => (
              <div key={f.title} className="flex items-start gap-3">
                <span className="mt-0.5 text-xl">{f.emoji}</span>
                <div>
                  <div className="text-sm font-bold">{f.title}</div>
                  <div className="text-xs text-white/30">{f.desc}</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 하단 */}
        <div className="relative z-10 px-12 pb-8 xl:px-16">
          <div className="flex items-center gap-4 text-xs text-white/20">
            <PokeBallSVG size={16} />
            <span>CodeDex &middot; 알고리즘 코딩 연습 플랫폼</span>
          </div>
        </div>
      </div>

      {/* 우측: 로그인 폼 */}
      <div className="flex flex-1 flex-col items-center justify-center px-6 py-12 lg:px-16">
        {/* 모바일 로고 */}
        <div className="mb-8 flex items-center gap-2 lg:hidden">
          <PokeBallSVG size={28} />
          <span className="text-lg font-extrabold">
            <span className="bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent">CodeDex</span>
          </span>
        </div>

        <div className="w-full max-w-sm animate-fade-in">
          {formContent}
        </div>
      </div>
    </div>
  );
}

function PokeBallSVG({ size }: { size: number }) {
  return (
    <svg viewBox="0 0 100 100" width={size} height={size} className="drop-shadow-md shrink-0">
      <defs>
        <linearGradient id={`pbRed${size}`} x1="0" x2="0" y1="0" y2="1">
          <stop offset="0" stopColor="#ff6b6b" /><stop offset="1" stopColor="#e03131" />
        </linearGradient>
      </defs>
      <circle cx="50" cy="50" r="46" fill="#1e1f3b" />
      <path d="M4,50 A46,46 0 0 1 96,50 Z" fill={`url(#pbRed${size})`} />
      <path d="M4,50 A46,46 0 0 0 96,50 Z" fill="#f0f0f0" />
      <rect x="4" y="46" width="92" height="8" fill="#1e1f3b" />
      <circle cx="50" cy="50" r="10" fill="#fff" stroke="#1e1f3b" strokeWidth="3" />
    </svg>
  );
}

function KakaoIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18">
      <path fill="#3C1E1E" d="M9 1C4.58 1 1 3.8 1 7.19c0 2.18 1.44 4.1 3.62 5.2L4 15.54c-.05.2.17.36.35.25l3.15-2.1c.49.07 1 .1 1.5.1 4.42 0 8-2.8 8-6.19S13.42 1 9 1z" />
    </svg>
  );
}

function NameForm({
  value, busy, error, submitLabel, busyLabel, onChange, onSubmit
}: {
  value: string; busy: boolean; error: string | null;
  submitLabel: string; busyLabel: string;
  onChange: (v: string) => void; onSubmit: (e: React.FormEvent) => void;
}) {
  return (
    <form className="mt-3 flex flex-col gap-3" onSubmit={onSubmit}>
      <input
        data-testid="trainer-name-input"
        autoFocus
        value={value}
        onChange={(e) => onChange(e.target.value)}
        maxLength={16}
        placeholder="트레이너 이름 (예: 지우)"
        className="rounded-xl border border-white/10 bg-white/[0.04] px-4 py-3 text-sm outline-none transition-colors placeholder:text-white/20 focus:border-amber-400/50 focus:bg-white/[0.06]"
      />
      {error && <p className="text-xs text-rose-300">{error}</p>}
      <button
        data-testid="trainer-name-submit"
        disabled={!value.trim() || busy}
        className="btn-primary disabled:opacity-40"
      >
        {busy ? busyLabel : submitLabel}
      </button>
    </form>
  );
}
