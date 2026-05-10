"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { useTrainer } from "@/components/TrainerProvider";

export default function LoginPage() {
  const router = useRouter();
  const { profile, ready, createTrainer } = useTrainer();
  const [busy, setBusy] = useState(false);

  async function startGuest() {
    setBusy(true);
    try {
      await createTrainer(`Guest${Date.now()}`.slice(0, 16));
      router.push("/");
    } finally {
      setBusy(false);
    }
  }

  if (!ready) {
    return <div className="text-sm text-zinc-400">로딩 중...</div>;
  }

  if (profile) {
    return (
      <section className="mx-auto max-w-xl rounded-2xl border border-white/10 bg-zinc-900/70 p-6">
        <div data-testid="login-current-session" className="text-sm text-zinc-300">
          이미 <b className="text-amber-200">{profile.name}</b> 세션으로 체험 중입니다.
        </div>
        <div className="mt-4 flex gap-2">
          <Link href="/" className="rounded-md bg-amber-500 px-3 py-2 text-sm font-bold text-zinc-950">
            메인으로 이동
          </Link>
          <Link href="/profile" className="rounded-md bg-zinc-800 px-3 py-2 text-sm font-bold text-zinc-100">
            로그인하고 저장하기
          </Link>
        </div>
      </section>
    );
  }

  return (
    <section className="mx-auto max-w-xl rounded-2xl border border-white/10 bg-zinc-900/70 p-6">
      <p className="text-xs font-semibold uppercase tracking-wider text-amber-300">DongJun CodeDex</p>
      <h1 className="mt-2 text-2xl font-bold">바로 체험하기</h1>
      <p className="mt-2 text-sm text-zinc-300">
        먼저 Guest 세션으로 문제 풀이를 시작하고, 원하면 나중에 카카오 계정으로 기록을 보관할 수 있습니다.
      </p>
      <button
        data-testid="guest-start"
        disabled={busy}
        onClick={startGuest}
        className="mt-6 w-full rounded-md bg-amber-500 px-4 py-3 text-sm font-bold text-zinc-950 hover:bg-amber-400 disabled:opacity-50"
      >
        {busy ? "Guest 세션 생성 중..." : "게스트로 체험하기"}
      </button>
      <p data-testid="guest-login-hint" className="mt-3 text-center text-xs text-zinc-400">
        체험 중에는 Guest 상태로 표시되며, 프로필에서 로그인하고 저장할 수 있습니다.
      </p>
    </section>
  );
}
