import Link from "next/link";
import { categories, problems } from "@/lib/dataset";

const TYPE_BG: Record<string, string> = {
  fighting:"bg-type-fighting", psychic:"bg-type-psychic", flying:"bg-type-flying",
  steel:"bg-type-steel", normal:"bg-type-normal", grass:"bg-type-grass",
  fire:"bg-type-fire", water:"bg-type-water", ice:"bg-type-ice",
  dragon:"bg-type-dragon", rock:"bg-type-rock", ghost:"bg-type-ghost",
  electric:"bg-type-electric", bug:"bg-type-bug", poison:"bg-type-poison",
  ground:"bg-type-ground", dark:"bg-type-dark", fairy:"bg-type-fairy"
};

export default function HomePage() {
  return (
    <div className="space-y-10">
      <section className="rounded-3xl border border-white/10 bg-gradient-to-br from-zinc-900 to-zinc-950 p-8">
        <h1 className="text-3xl font-bold sm:text-4xl">
          백준이 닫혔다고? <span className="text-amber-400">도감으로 잡으면 된다.</span>
        </h1>
        <p className="mt-3 max-w-2xl text-sm text-zinc-400">
          22개 알고리즘 분류 = 18개 포켓몬 타입. {problems.length}마리의 코드 몬스터를 잡아 진화시키세요.
          정답 코드를 <b>Oracle</b> 로 두고 입력 생성기로 생성한 케이스로 자동 채점합니다.
        </p>
        <div className="mt-5 flex flex-wrap gap-3 text-sm">
          <Stat label="분류 (타입)" value={categories.length} />
          <Stat label="총 몬스터" value={problems.length} />
          <Stat label="채점 모드" value="Harness · Oracle" />
        </div>
      </section>

      <section>
        <h2 className="mb-4 text-xl font-bold">분류별 도감</h2>
        <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {categories.map((c) => (
            <Link key={c.slug} href={`/category/${c.slug}`} className="pixel-card p-5">
              <div className="flex items-start justify-between">
                <div>
                  <div className="text-lg font-bold">{c.name_ko}</div>
                  <div className="text-xs text-zinc-400">{c.name_en}</div>
                </div>
                <span className={`pill text-white ${TYPE_BG[c.type] ?? "bg-zinc-700"}`}>
                  {c.type}
                </span>
              </div>
              <div className="mt-4 flex items-end justify-between">
                <div className="text-sm text-zinc-300">{c.problemCount} 마리</div>
                <div className="text-xs text-zinc-500">→ 도감 열기</div>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}

function Stat({ label, value }: { label: string; value: string | number }) {
  return (
    <div className="rounded-xl border border-white/10 bg-zinc-900 px-4 py-2">
      <div className="text-[10px] uppercase tracking-wider text-zinc-500">{label}</div>
      <div className="text-base font-semibold">{value}</div>
    </div>
  );
}
