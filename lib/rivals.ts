// 시드된 라이벌 트레이너 — 결정적 진행률로 생성.
// 본인 + 라이벌 N명을 함께 정렬해 리더보드를 의미 있게 만든다.
// "나"의 데이터는 외부에서 주입.

export type Rival = {
  id: string;
  name: string;
  emoji: string;
  tr: number;
  dexPct: number;       // 0~1
};

const SEEDS: Array<Pick<Rival, "id" | "name" | "emoji"> & { skill: number }> = [
  { id: "red",     name: "레드",     emoji: "🧢", skill: 0.96 },
  { id: "blue",    name: "블루",     emoji: "🟦", skill: 0.92 },
  { id: "green",   name: "그린",     emoji: "🟩", skill: 0.88 },
  { id: "yellow",  name: "옐로",     emoji: "🟨", skill: 0.85 },
  { id: "gold",    name: "골드",     emoji: "🟡", skill: 0.82 },
  { id: "silver",  name: "실버",     emoji: "⚪", skill: 0.78 },
  { id: "crystal", name: "크리스탈", emoji: "💠", skill: 0.74 },
  { id: "ruby",    name: "루비",     emoji: "🔴", skill: 0.7  },
  { id: "sapphire",name: "사파이어", emoji: "🔷", skill: 0.66 },
  { id: "emerald", name: "에메랄드", emoji: "🟢", skill: 0.62 },
  { id: "rocket",  name: "로켓단R",  emoji: "🚀", skill: 0.55 },
  { id: "newbie",  name: "지나가던훈련생", emoji: "🎒", skill: 0.42 }
];

// skill 0~1 → TR 600~1950 매핑 (약간의 결정적 노이즈)
function skillToTR(seedId: string, skill: number): number {
  // 단순 hash 기반 노이즈
  let h = 0;
  for (let i = 0; i < seedId.length; i++) h = (h * 31 + seedId.charCodeAt(i)) | 0;
  const noise = ((h >>> 0) % 80) - 40;
  return Math.round(600 + skill * 1350 + noise);
}

export function rivalLeaderboard(totalProblems: number): Rival[] {
  return SEEDS.map((s) => ({
    id: s.id,
    name: s.name,
    emoji: s.emoji,
    tr: skillToTR(s.id, s.skill),
    dexPct: Math.min(0.99, s.skill * (0.55 + ((s.id.length * 7) % 30) / 100))
  })).map((r) => ({
    ...r,
    // dexPct → 잡은 마릿수
    dexPct: Math.round(r.dexPct * totalProblems) / totalProblems
  }));
}
