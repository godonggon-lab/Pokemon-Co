import { NextResponse } from "next/server";
import { listAuthAccounts } from "@/lib/db";
import { currentTrainer } from "@/lib/session";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  const trainer = currentTrainer();
  if (!trainer) return NextResponse.json({ accounts: [] });
  return NextResponse.json({ accounts: listAuthAccounts(trainer.id) });
}
