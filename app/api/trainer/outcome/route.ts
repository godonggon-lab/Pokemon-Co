// POST /api/trainer/outcome
//   { problemSlug, problemR, expected, k, delta, prevTR, nextTR, outcome: "win"|"loss" }
import { NextResponse } from "next/server";
import { applyLoss, applyWin, type ApplyOutcomeArgs } from "@/lib/db";
import { currentTrainer } from "@/lib/session";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  const t = currentTrainer();
  if (!t) return NextResponse.json({ error: "unauthorized" }, { status: 401 });
  const body = await req.json().catch(() => null);
  if (!body || typeof body !== "object") return NextResponse.json({ error: "bad input" }, { status: 400 });

  const args: ApplyOutcomeArgs = {
    problemSlug: String(body.problemSlug),
    problemR:    Math.round(Number(body.problemR)),
    expected:    Number(body.expected),
    k:           Math.round(Number(body.k)),
    delta:       Math.round(Number(body.delta)),
    prevTR:      Math.round(Number(body.prevTR)),
    nextTR:      Math.round(Number(body.nextTR)),
    outcome:     body.outcome === "win" ? "win" : "loss"
  };
  if (!args.problemSlug || !Number.isFinite(args.nextTR)) {
    return NextResponse.json({ error: "bad input" }, { status: 400 });
  }
  if (args.outcome === "win") {
    const r = applyWin(t.id, args);
    return NextResponse.json({ ok: true, firstCapture: r.firstCapture });
  } else {
    applyLoss(t.id, args);
    return NextResponse.json({ ok: true });
  }
}
