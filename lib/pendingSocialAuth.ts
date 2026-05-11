import crypto from "node:crypto";
import { cookies } from "next/headers";
import type { SocialProfile } from "./socialAuth";

const COOKIE = "dj_pending_social";
const MAX_AGE = 60 * 10;

function secret() {
  return process.env.AUTH_COOKIE_SECRET
    ?? process.env.KAKAO_CLIENT_SECRET
    ?? process.env.NAVER_CLIENT_SECRET
    ?? "dongjun-dev-pending-social";
}

function sign(payload: string) {
  return crypto.createHmac("sha256", secret()).update(payload).digest("base64url");
}

export function setPendingSocialProfile(profile: SocialProfile) {
  const payload = Buffer.from(JSON.stringify(profile), "utf8").toString("base64url");
  cookies().set(COOKIE, `${payload}.${sign(payload)}`, {
    httpOnly: true,
    sameSite: "lax",
    path: "/",
    maxAge: MAX_AGE,
    secure: process.env.NODE_ENV === "production"
  });
}

export function getPendingSocialProfile(): SocialProfile | null {
  const raw = cookies().get(COOKIE)?.value;
  if (!raw) return null;
  const [payload, sig] = raw.split(".");
  if (!payload || !sig || sign(payload) !== sig) return null;
  try {
    const profile = JSON.parse(Buffer.from(payload, "base64url").toString("utf8"));
    if (profile?.provider !== "kakao" && profile?.provider !== "naver") return null;
    if (typeof profile?.providerUserId !== "string" || !profile.providerUserId) return null;
    return profile;
  } catch {
    return null;
  }
}

export function clearPendingSocialProfile() {
  cookies().delete(COOKIE);
}
