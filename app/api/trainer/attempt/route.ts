// POST /api/trainer/attempt  { problemSlug }
import { NextResponse } from "next/server";
import { bumpAttempt } from "@/lib/db";
import { currentTrainer } from "@/lib/session";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  const t = currentTrainer();
  if (!t) return NextResponse.json({ error: "unauthorized" }, { status: 401 });
  const { problemSlug } = await req.json().catch(() => ({}));
  if (typeof problemSlug !== "string") return NextResponse.json({ error: "bad input" }, { status: 400 });
  bumpAttempt(t.id, problemSlug);
  return NextResponse.json({ ok: true });
}
