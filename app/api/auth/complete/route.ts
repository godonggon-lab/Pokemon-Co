import { NextResponse } from "next/server";
import { createTrainer, findTrainerByAuthAccount, linkAuthAccount } from "@/lib/db";
import { clearPendingSocialProfile, getPendingSocialProfile } from "@/lib/pendingSocialAuth";
import { setSessionCookie } from "@/lib/session";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  const pending = getPendingSocialProfile();
  if (!pending) {
    return NextResponse.json({ error: "pending social login not found" }, { status: 400 });
  }

  let body: any;
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "invalid json" }, { status: 400 });
  }

  const name = String(body?.name ?? "").trim();
  if (!name || name.length > 16) {
    return NextResponse.json({ error: "이름은 1-16자" }, { status: 400 });
  }

  const existing = findTrainerByAuthAccount(pending.provider, pending.providerUserId);
  if (existing) {
    setSessionCookie(existing.trainer.id, existing.secret);
    clearPendingSocialProfile();
    return NextResponse.json({ ok: true, mode: "signed_in" });
  }

  try {
    const { trainer, secret } = createTrainer(name);
    linkAuthAccount({
      trainerId: trainer.id,
      provider: pending.provider,
      providerUserId: pending.providerUserId,
      email: pending.email,
      displayName: pending.displayName
    });
    setSessionCookie(trainer.id, secret);
    clearPendingSocialProfile();
    return NextResponse.json({ ok: true, mode: "linked" });
  } catch (e: any) {
    return NextResponse.json({ error: e?.message ?? "fail" }, { status: 400 });
  }
}
