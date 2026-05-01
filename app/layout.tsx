import "./globals.css";
import type { Metadata } from "next";
import Link from "next/link";
import { TrainerProvider } from "@/components/TrainerProvider";
import TrainerHUD from "@/components/TrainerHUD";

export const metadata: Metadata = {
  title: "DongJun CodeDex — 코딩테스트 도감",
  description: "포켓몬 도감 컨셉의 BOJ 코딩테스트 학습 사이트 (하네스 엔지니어링 적용)"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko">
      <body>
        <TrainerProvider>
          <header className="sticky top-0 z-40 border-b border-white/10 bg-zinc-950/80 backdrop-blur">
            <div className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3">
              <Link href="/" className="flex items-center gap-2 text-lg font-bold tracking-tight">
                <span className="inline-block h-7 w-7 rounded-full bg-gradient-to-br from-rose-500 to-amber-400 ring-2 ring-white/20" />
                <span>CodeDex</span>
                <span className="hidden text-xs font-normal text-zinc-400 md:inline">코딩테스트 도감</span>
              </Link>
              <nav className="flex flex-1 items-center justify-end gap-4 text-sm text-zinc-300">
                <Link href="/" className="hover:text-white">도감</Link>
                <Link href="/problems" className="hover:text-white">전체</Link>
                <Link href="/leaderboard" className="hover:text-white">리더보드</Link>
                <Link href="/profile" className="hover:text-white">프로필</Link>
                <TrainerHUD />
              </nav>
            </div>
          </header>
          <main className="mx-auto max-w-6xl px-4 py-8">{children}</main>
          <footer className="mx-auto max-w-6xl px-4 py-10 text-center text-xs text-zinc-500">
            정답 코드를 Oracle 로 사용하는 하네스 채점 시스템 · 학습용
          </footer>
        </TrainerProvider>
      </body>
    </html>
  );
}
