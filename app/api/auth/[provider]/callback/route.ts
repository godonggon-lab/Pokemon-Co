import { NextResponse } from "next/server";
import {
  findTrainerByAuthAccount,
  linkAuthAccount
} from "@/lib/db";
import { setPendingSocialProfile } from "@/lib/pendingSocialAuth";
import { currentTrainer, setSessionCookie } from "@/lib/session";
import {
  authStateCookie,
  exchangeCodeForProfile,
  parseProvider
} from "@/lib/socialAuth";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET(
  req: Request,
  { params }: { params: { provider: string } }
) {
  const provider = parseProvider(params.provider);
  const url = new URL(req.url);
  const redirect = new URL("/profile", req.url);
  const errorRedirect = new URL("/login", req.url);

  if (!provider) {
    errorRedirect.searchParams.set("auth_error", "unsupported_provider");
    return NextResponse.redirect(errorRedirect);
  }

  const code = url.searchParams.get("code");
  const state = url.searchParams.get("state");
  const mockOAuth = process.env.E2E_MOCK_OAUTH === "1" && code?.startsWith("mock-");
  const savedState = req.headers.get("cookie")
    ?.split(";")
    .map((v) => v.trim())
    .find((v) => v.startsWith(`${authStateCookie(provider)}=`))
    ?.split("=")[1];

  if (!code || (!mockOAuth && (!state || !savedState || state !== savedState))) {
    errorRedirect.searchParams.set("auth_error", "invalid_state");
    return NextResponse.redirect(errorRedirect);
  }

  try {
    const profile = await exchangeCodeForProfile(provider, code, url.origin);
    if (!profile.providerUserId) throw new Error("provider user id missing");

    const existing = findTrainerByAuthAccount(provider, profile.providerUserId);
    if (existing) {
      setSessionCookie(existing.trainer.id, existing.secret);
      redirect.searchParams.set("auth", "signed_in");
    } else {
      const trainer = currentTrainer();
      if (!trainer) {
        const signup = new URL("/login", req.url);
        signup.searchParams.set("auth", "signup_required");
        setPendingSocialProfile(profile);
        const res = NextResponse.redirect(signup);
        res.cookies.delete(authStateCookie(provider));
        return res;
      }
      linkAuthAccount({
        trainerId: trainer.id,
        provider,
        providerUserId: profile.providerUserId,
        email: profile.email,
        displayName: profile.displayName
      });
      redirect.searchParams.set("auth", "linked");
    }

    const res = NextResponse.redirect(redirect);
    res.cookies.delete(authStateCookie(provider));
    return res;
  } catch (e: any) {
    errorRedirect.searchParams.set("auth_error", e?.message ?? "auth_failed");
    return NextResponse.redirect(errorRedirect);
  }
}
