import Link from "next/link";
import { Suspense } from "react";
import { categories, problems } from "@/lib/dataset";
import HomeLoginGate from "@/components/HomeLoginGate";

const TYPE_BG: Record<string, string> = {
  fighting:"bg-type-fighting", psychic:"bg-type-psychic", flying:"bg-type-flying",
  steel:"bg-type-steel", normal:"bg-type-normal", grass:"bg-type-grass",
  fire:"bg-type-fire", water:"bg-type-water", ice:"bg-type-ice",
  dragon:"bg-type-dragon", rock:"bg-type-rock", ghost:"bg-type-ghost",
  electric:"bg-type-electric", bug:"bg-type-bug", poison:"bg-type-poison",
  ground:"bg-type-ground", dark:"bg-type-dark", fairy:"bg-type-fairy"
};

const TYPE_EMOJI: Record<string, string> = {
  fighting: "🥊", psychic: "🔮", flying: "🦅", steel: "⚙️",
  normal: "⭐", grass: "🌿", fire: "🔥", water: "💧",
  ice: "❄️", dragon: "🐉", rock: "🪨", ghost: "👻",
  electric: "⚡", bug: "🐛", poison: "☠️", ground: "🏔️",
  dark: "🌑", fairy: "✨"
};

export default function HomePage() {
  return (
    <Suspense fallback={<div className="text-sm text-white/40">로딩 중...</div>}>
    <HomeLoginGate>
    <div className="space-y-10">
      {/* 히어로 섹션 */}
      <section className="poke-card overflow-hidden">
        <div className="relative px-8 py-10">
          {/* 배경 장식 */}
          <div className="pointer-events-none absolute right-0 top-0 h-full w-1/3 opacity-[0.04]">
            <svg viewBox="0 0 100 100" className="h-full w-full">
              <circle cx="50" cy="50" r="46" fill="none" stroke="white" strokeWidth="2" />
              <path d="M4,50 A46,46 0 0 1 96,50" fill="none" stroke="white" strokeWidth="2" />
              <circle cx="50" cy="50" r="10" fill="none" stroke="white" strokeWidth="2" />
            </svg>
          </div>

          <div className="relative">
            <div className="inline-flex items-center gap-2 rounded-full bg-amber-500/10 px-3 py-1 text-xs font-bold text-amber-300">
              <span>🔥</span> {categories.length}개 알고리즘 · {problems.length}마리 몬스터
            </div>
            <h1 className="mt-4 text-3xl font-extrabold tracking-tight sm:text-4xl">
              알고리즘 몬스터를<br />
              <span className="bg-gradient-to-r from-amber-300 via-orange-400 to-rose-400 bg-clip-text text-transparent">
                잡아서 성장하자!
              </span>
            </h1>
            <p className="mt-4 max-w-xl text-sm leading-relaxed text-white/50">
              각 알고리즘 분류가 포켓몬 타입과 매칭되어 있어요.
              문제를 풀면 몬스터를 포획하고, 트레이너 레이팅이 올라가요!
            </p>
          </div>

          <div className="relative mt-6 flex flex-wrap gap-3">
            <StatChip emoji="📖" label="분류" value={`${categories.length}개 타입`} />
            <StatChip emoji="🎯" label="몬스터" value={`${problems.length}마리`} />
            <StatChip emoji="⚔️" label="채점" value="자동 채점" />
          </div>
        </div>
      </section>

      {/* 알고리즘 분류 그리드 */}
      <section>
        <h2 className="section-title mb-5 flex items-center gap-2">
          <span>📖</span> 알고리즘 도감
        </h2>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {categories.map((c) => (
            <Link
              key={c.slug}
              href={`/category/${c.slug}`}
              className="group poke-card overflow-hidden p-0"
            >
              {/* 타입 컬러 상단 바 */}
              <div className={`h-1 ${TYPE_BG[c.type] ?? "bg-zinc-700"}`} />
              <div className="flex items-center gap-4 px-5 py-4">
                {/* 타입 아이콘 */}
                <div className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-xl text-2xl ${TYPE_BG[c.type] ?? "bg-zinc-700"} bg-opacity-20`}
                     style={{ backgroundColor: `${typeColor(c.type)}15` }}>
                  {TYPE_EMOJI[c.type] ?? "❓"}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-baseline gap-2">
                    <span className="text-base font-extrabold group-hover:text-amber-300 transition-colors">{c.name_ko}</span>
                    <span className="text-xs text-white/30">{c.name_en}</span>
                  </div>
                  <div className="mt-1 flex items-center gap-2">
                    <span className={`pill text-white text-[10px] ${TYPE_BG[c.type] ?? "bg-zinc-700"}`}>
                      {c.type}
                    </span>
                    <span className="text-xs text-white/40">{c.problemCount}마리</span>
                  </div>
                </div>
                <span className="text-white/20 transition-all group-hover:translate-x-1 group-hover:text-amber-400">
                  →
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </div>
    </HomeLoginGate>
    </Suspense>
  );
}

function StatChip({ emoji, label, value }: { emoji: string; label: string; value: string }) {
  return (
    <div className="flex items-center gap-2 rounded-xl border border-white/[0.06] bg-white/[0.03] px-4 py-2.5">
      <span className="text-lg">{emoji}</span>
      <div>
        <div className="text-[10px] font-semibold uppercase text-white/30">{label}</div>
        <div className="text-sm font-bold">{value}</div>
      </div>
    </div>
  );
}

function typeColor(type: string): string {
  const colors: Record<string, string> = {
    fighting: "#C03028", psychic: "#F85888", flying: "#A890F0", steel: "#B8B8D0",
    normal: "#A8A878", grass: "#78C850", fire: "#F08030", water: "#6890F0",
    ice: "#98D8D8", dragon: "#7038F8", rock: "#B8A038", ghost: "#705898",
    electric: "#F8D030", bug: "#A8B820", poison: "#A040A0", ground: "#E0C068",
    dark: "#705848", fairy: "#EE99AC"
  };
  return colors[type] ?? "#888888";
}
