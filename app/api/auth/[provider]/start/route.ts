import { NextResponse } from "next/server";
import crypto from "node:crypto";
import { authStateCookie, buildAuthorizeUrl, parseProvider } from "@/lib/socialAuth";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET(
  req: Request,
  { params }: { params: { provider: string } }
) {
  const provider = parseProvider(params.provider);
  if (!provider) {
    return NextResponse.json({ error: "unsupported provider" }, { status: 404 });
  }

  const requestUrl = new URL(req.url);
  const state = crypto.randomBytes(24).toString("hex");
  const url = buildAuthorizeUrl(provider, state, requestUrl.origin);
  if (!url) {
    return NextResponse.redirect(new URL(`/login?auth_error=${provider}_not_configured`, req.url));
  }

  const mockUser = requestUrl.searchParams.get("mock_user")?.replace(/[^a-zA-Z0-9_-]/g, "").slice(0, 48);
  const mockCode = mockUser ? `mock-${mockUser}` : `mock-${Date.now()}`;
  const target = process.env.E2E_MOCK_OAUTH === "1"
    ? new URL(`/api/auth/${provider}/callback?code=${mockCode}&state=${state}`, req.url)
    : url;

  const res = NextResponse.redirect(target);
  res.cookies.set(authStateCookie(provider), state, {
    httpOnly: true,
    sameSite: "lax",
    path: "/",
    maxAge: 60 * 10,
    secure: process.env.NODE_ENV === "production"
  });
  return res;
}
