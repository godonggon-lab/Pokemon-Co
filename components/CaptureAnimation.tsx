"use client";

// AC 시 화면 중앙에 떠서 흔들리는 몬스터볼 → 캡처 성공 토스트.

import { useEffect, useState } from "react";
import Sprite from "./Sprite";

export type CaptureEvent = {
  monsterName: string;
  spriteUrl: string;
  fallbackEmoji: string;
  delta: number;     // TR 변동
  newTR: number;
  firstCapture: boolean;
};

export default function CaptureAnimation({
  event, onDone
}: { event: CaptureEvent | null; onDone: () => void }) {
  const [phase, setPhase] = useState<"hidden" | "throw" | "wiggle" | "caught" | "toast">("hidden");

  useEffect(() => {
    if (!event) { setPhase("hidden"); return; }
    setPhase("throw");
    const t1 = setTimeout(() => setPhase("wiggle"),  450);
    const t2 = setTimeout(() => setPhase("caught"),  1700);
    const t3 = setTimeout(() => setPhase("toast"),   2100);
    const t4 = setTimeout(() => { setPhase("hidden"); onDone(); }, 3800);
    return () => { [t1,t2,t3,t4].forEach(clearTimeout); };
  }, [event, onDone]);

  if (!event || phase === "hidden") return null;

  const inFlight = phase === "throw" || phase === "wiggle" || phase === "caught";

  return (
    <>
      <style jsx global>{`
        @keyframes ball-throw   { from { transform: translate(-200px, -240px) rotate(-540deg); opacity: 0 } to { transform: translate(0,0) rotate(0); opacity: 1 } }
        @keyframes ball-wiggle  { 0%,100% { transform: rotate(0) } 25% { transform: rotate(-22deg) } 75% { transform: rotate(22deg) } }
        @keyframes ball-pop     { 0% { transform: scale(1) } 60% { transform: scale(1.35) } 100% { transform: scale(1) } }
        @keyframes toast-in     { from { transform: translate(-50%, 30px); opacity: 0 } to { transform: translate(-50%, 0); opacity: 1 } }
      `}</style>

      {inFlight && (
        <div className="fixed inset-0 z-50 flex items-center justify-center pointer-events-none">
          <div className="relative flex flex-col items-center">
            {phase === "caught" && (
              <div className="absolute -top-28 flex flex-col items-center"
                   style={{ animation: "ball-pop 0.5s ease-out" }}>
                <Sprite src={event.spriteUrl} alt={event.monsterName}
                        fallback={event.fallbackEmoji} size={96} pixelated={false} />
                <div className="text-xs text-amber-300 drop-shadow">✨ {event.monsterName} ✨</div>
              </div>
            )}
            <div
              className="relative h-20 w-20"
              style={{
                animation:
                  phase === "throw"  ? "ball-throw 0.5s ease-out forwards" :
                  phase === "wiggle" ? "ball-wiggle 0.45s ease-in-out 3"   :
                  phase === "caught" ? "ball-pop 0.5s ease-out"            :
                  undefined
              }}
            >
              {/* 몬스터볼 SVG */}
              <svg viewBox="0 0 100 100" className="drop-shadow-[0_4px_8px_rgba(0,0,0,0.6)]">
                <defs>
                  <linearGradient id="topRed" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="0" stopColor="#ff6b6b" />
                    <stop offset="1" stopColor="#c92a2a" />
                  </linearGradient>
                  <linearGradient id="botWhite" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="0" stopColor="#ffffff" />
                    <stop offset="1" stopColor="#cfcfcf" />
                  </linearGradient>
                </defs>
                <circle cx="50" cy="50" r="46" fill="#222" />
                <path d="M4,50 A46,46 0 0 1 96,50 Z" fill="url(#topRed)" />
                <path d="M4,50 A46,46 0 0 0 96,50 Z" fill="url(#botWhite)" />
                <rect x="4" y="46" width="92" height="8" fill="#222" />
                <circle cx="50" cy="50" r="11" fill="#fff" stroke="#222" strokeWidth="3" />
                <circle cx="50" cy="50" r="5"  fill="#eee" stroke="#222" strokeWidth="2" />
              </svg>
            </div>
          </div>
        </div>
      )}

      {phase === "toast" && (
        <div
          className="fixed left-1/2 top-20 z-50 -translate-x-1/2 rounded-2xl border border-amber-400/30 bg-zinc-900/95 px-5 py-3 shadow-2xl"
          style={{ animation: "toast-in 0.3s ease-out" }}
        >
          <div className="flex items-center gap-3">
            <Sprite src={event.spriteUrl} alt={event.monsterName}
                    fallback={event.fallbackEmoji} size={56} pixelated={false} />
            <div>
              <div className="text-sm font-bold">
                {event.firstCapture ? "포획 성공!" : "다시 만났다!"}
              </div>
              <div className="text-xs text-zinc-300">
                <b>{event.monsterName}</b>이(가) 도감에 등록되었습니다.
              </div>
              <div className="mt-0.5 text-[11px] text-amber-300">
                TR {event.delta >= 0 ? "+" : ""}{event.delta} → {event.newTR}
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
