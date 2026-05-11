import "./globals.css";
import type { Metadata } from "next";
import Link from "next/link";
import { TrainerProvider } from "@/components/TrainerProvider";
import TrainerHUD from "@/components/TrainerHUD";

export const metadata: Metadata = {
  title: "CodeDex - 알고리즘 도감",
  description: "포켓몬 도감 컨셉으로 즐기는 알고리즘 코딩 연습"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ko">
      <body>
        <TrainerProvider>
          <header className="sticky top-0 z-40 border-b border-white/[0.06]" style={{ background: "rgba(18,19,42,0.92)", backdropFilter: "blur(12px)" }}>
            <div className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3">
              <Link href="/" className="flex items-center gap-2.5 font-extrabold tracking-tight text-lg group">
                {/* 포켓볼 로고 */}
                <span className="relative inline-flex h-8 w-8 items-center justify-center">
                  <svg viewBox="0 0 100 100" className="h-8 w-8 drop-shadow-md group-hover:animate-wiggle transition-transform">
                    <defs>
                      <linearGradient id="navTopRed" x1="0" x2="0" y1="0" y2="1">
                        <stop offset="0" stopColor="#ff6b6b" />
                        <stop offset="1" stopColor="#e03131" />
                      </linearGradient>
                    </defs>
                    <circle cx="50" cy="50" r="46" fill="#2a2b4a" />
                    <path d="M4,50 A46,46 0 0 1 96,50 Z" fill="url(#navTopRed)" />
                    <path d="M4,50 A46,46 0 0 0 96,50 Z" fill="#f0f0f0" />
                    <rect x="4" y="46" width="92" height="8" fill="#2a2b4a" />
                    <circle cx="50" cy="50" r="10" fill="#fff" stroke="#2a2b4a" strokeWidth="3" />
                  </svg>
                </span>
                <span className="bg-gradient-to-r from-amber-300 to-orange-400 bg-clip-text text-transparent">CodeDex</span>
              </Link>
              <nav className="flex flex-1 items-center justify-end gap-1 text-sm">
                <NavLink href="/" label="도감" emoji="📖" />
                <NavLink href="/problems" label="전체" emoji="📋" />
                <NavLink href="/leaderboard" label="랭킹" emoji="🏆" />
                <NavLink href="/profile" label="프로필" emoji="👤" />
                <div className="ml-2">
                  <TrainerHUD />
                </div>
              </nav>
            </div>
          </header>
          <main className="mx-auto max-w-6xl px-4 py-8 animate-fade-in">{children}</main>
          <footer className="mx-auto max-w-6xl px-4 py-10 text-center text-xs text-white/30">
            CodeDex · 알고리즘을 잡아서 실력을 키우자 🎮
          </footer>
        </TrainerProvider>
      </body>
    </html>
  );
}

function NavLink({ href, label, emoji }: { href: string; label: string; emoji: string }) {
  return (
    <Link
      href={href}
      className="flex items-center gap-1.5 rounded-lg px-3 py-2 text-white/60 transition-all hover:bg-white/[0.06] hover:text-white"
    >
      <span className="text-base">{emoji}</span>
      <span className="hidden font-semibold sm:inline">{label}</span>
    </Link>
  );
}
