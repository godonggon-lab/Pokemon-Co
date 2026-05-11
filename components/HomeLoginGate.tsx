"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { useTrainer } from "./TrainerProvider";

export default function HomeLoginGate({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const { profile, ready } = useTrainer();

  useEffect(() => {
    if (ready && !profile) {
      router.replace("/login");
    }
  }, [profile, ready, router]);

  if (!ready) {
    return <div className="text-sm text-zinc-400">로딩 중...</div>;
  }

  if (!profile) {
    return <div className="text-sm text-zinc-400">로그인 화면으로 이동 중...</div>;
  }

  return <>{children}</>;
}
