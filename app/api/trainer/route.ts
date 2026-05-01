// 트레이너 CRUD.
// GET  /api/trainer        - 현재 세션의 트레이너 (없으면 null)
// POST /api/trainer        - 새 트레이너 생성 + 세션 쿠키 발급 { name }
// DELETE /api/trainer      - 로그아웃

import { NextResponse } from "next/server";
import { createTrainer, listAttempts, listCaptures, recentHistory } from "@/lib/db";
import { clearSessionCookie, currentTrainer, setSessionCookie } from "@/lib/session";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  const t = currentTrainer();
  if (!t) return NextResponse.json({ trainer: null });
  return NextResponse.json({
    trainer: t,
    attempts: listAttempts(t.id),
    captures: listCaptures(t.id),
    history:  recentHistory(t.id, 30)
  });
}

export async function POST(req: Request) {
  let body: any;
  try { body = await req.json(); } catch { return NextResponse.json({ error: "invalid json" }, { status: 400 }); }
  const name = String(body?.name ?? "").trim();
  if (!name || name.length > 16) return NextResponse.json({ error: "이름은 1-16자" }, { status: 400 });
  try {
    const { trainer, secret } = createTrainer(name);
    setSessionCookie(trainer.id, secret);
    return NextResponse.json({
      trainer, attempts: {}, captures: [], history: []
    });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message ?? "fail" }, { status: 400 });
  }
}

export async function DELETE() {
  clearSessionCookie();
  return NextResponse.json({ ok: true });
}
