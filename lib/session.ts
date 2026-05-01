// 세션 쿠키 헬퍼.
// dj_session = "<trainerId>:<secret>"  (httpOnly, sameSite=lax)

import { cookies } from "next/headers";
import { authenticate, type DbTrainer } from "./db";

const COOKIE = "dj_session";
const MAX_AGE = 60 * 60 * 24 * 365; // 1년

export function setSessionCookie(trainerId: number, secret: string) {
  cookies().set(COOKIE, `${trainerId}:${secret}`, {
    httpOnly: true,
    sameSite: "lax",
    path: "/",
    maxAge: MAX_AGE,
    secure: process.env.NODE_ENV === "production"
  });
}

export function clearSessionCookie() {
  cookies().delete(COOKIE);
}

export function currentTrainer(): DbTrainer | null {
  const c = cookies().get(COOKIE)?.value;
  if (!c) return null;
  const [idStr, secret] = c.split(":");
  const id = Number(idStr);
  if (!Number.isFinite(id) || !secret) return null;
  return authenticate(id, secret);
}
