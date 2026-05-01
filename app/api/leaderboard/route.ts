// GET /api/leaderboard?limit=50
import { NextResponse } from "next/server";
import { leaderboardTop } from "@/lib/db";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET(req: Request) {
  const url = new URL(req.url);
  const limit = Math.min(200, Math.max(1, Number(url.searchParams.get("limit") ?? "50")));
  return NextResponse.json({ trainers: leaderboardTop(limit) });
}
