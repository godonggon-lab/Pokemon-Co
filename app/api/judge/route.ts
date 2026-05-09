// 채점 API: 프론트 → 이 라우트 → Judge 서비스(Docker 샌드박스, 기본 :5050)
//
// 보안:
// - 사용자 코드는 절대 Next 서버 프로세스 안에서 실행되지 않는다.
// - Judge 서비스가 격리된 Docker 컨테이너 안에서 실행한다.
// - 이 라우트는 단순 프록시 + 입력/응답 검증.

import { NextResponse } from "next/server";
import { getProblem } from "@/lib/dataset";

export const runtime = "nodejs";

const JUDGE_URL = process.env.JUDGE_URL ?? "http://127.0.0.1:5050/judge";
const JUDGE_RUN_URL = process.env.JUDGE_RUN_URL ?? JUDGE_URL.replace(/\/judge$/, "/run");
const MAX_CODE_BYTES = intEnv("JUDGE_MAX_CODE_BYTES", 64 * 1024);
const MAX_STDIN_BYTES = intEnv("JUDGE_MAX_STDIN_BYTES", 64 * 1024);
const MAX_OUTPUT_BYTES = intEnv("JUDGE_MAX_OUTPUT_BYTES", 64 * 1024 * 1024);
const RATE_LIMIT_WINDOW_MS = intEnv("JUDGE_RATE_LIMIT_WINDOW_MS", 60_000);
const RATE_LIMIT_MAX = intEnv("JUDGE_RATE_LIMIT_MAX", 20);

const rateBuckets = new Map<string, { count: number; resetAt: number }>();

// 사용자 제출 허용 언어는 python / cpp / java 로 통일.
// (oracle 코드는 어떤 언어든 사용 가능 — 출력만 같으면 되므로.)
const ALLOWED_LANGS = new Set([
  "python", "cpp", "java"
]);

function intEnv(name: string, fallback: number): number {
  const value = Number(process.env[name]);
  return Number.isFinite(value) && value > 0 ? Math.floor(value) : fallback;
}

function clientKey(req: Request): string {
  const forwarded = req.headers.get("x-forwarded-for")?.split(",")[0]?.trim();
  return forwarded || req.headers.get("x-real-ip") || "local";
}

function checkRateLimit(key: string) {
  const now = Date.now();
  const cur = rateBuckets.get(key);
  if (!cur || cur.resetAt <= now) {
    rateBuckets.set(key, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return { ok: true, remaining: RATE_LIMIT_MAX - 1, resetAt: now + RATE_LIMIT_WINDOW_MS };
  }
  if (cur.count >= RATE_LIMIT_MAX) {
    return { ok: false, remaining: 0, resetAt: cur.resetAt };
  }
  cur.count += 1;
  return { ok: true, remaining: RATE_LIMIT_MAX - cur.count, resetAt: cur.resetAt };
}

export async function POST(req: Request) {
  const limited = checkRateLimit(clientKey(req));
  if (!limited.ok) {
    return NextResponse.json(
      { status: "ERR", message: "rate limit exceeded" },
      {
        status: 429,
        headers: { "retry-after": String(Math.ceil((limited.resetAt - Date.now()) / 1000)) }
      }
    );
  }

  let body: any;
  try { body = await req.json(); }
  catch { return NextResponse.json({ status: "ERR", message: "invalid json" }, { status: 400 }); }

  const { problemSlug, lang, code, limits, mode, stdin } = body ?? {};
  if (typeof problemSlug !== "string" || typeof lang !== "string" || typeof code !== "string") {
    return NextResponse.json({ status: "ERR", message: "missing fields" }, { status: 400 });
  }
  if (!ALLOWED_LANGS.has(lang)) {
    return NextResponse.json({ status: "ERR", message: `lang not supported: ${lang}` }, { status: 400 });
  }
  if (Buffer.byteLength(code, "utf8") > MAX_CODE_BYTES) {
    return NextResponse.json({ status: "ERR", message: "code too large" }, { status: 413 });
  }
  if (mode === "run" && Buffer.byteLength(String(stdin ?? ""), "utf8") > MAX_STDIN_BYTES) {
    return NextResponse.json({ status: "ERR", message: "stdin too large" }, { status: 413 });
  }
  const problem = getProblem(problemSlug);
  if (!problem) {
    return NextResponse.json({ status: "ERR", message: "problem not found" }, { status: 404 });
  }
  // Oracle: 같은 분류·문제의 솔루션 중, 가능하면 같은 언어 우선.
  const oracle = problem.sources.find((s) => s.lang === lang) ?? problem.sources[0];
  if (!oracle) {
    return NextResponse.json({ status: "ERR", message: "no oracle source" }, { status: 500 });
  }

  try {
    const normalizedLimits = (limits && typeof limits === "object") ? {
      timeLimitMs:  Math.max(500, Math.min(10000, Number(limits.timeLimitMs)  || 2000)),
      memoryLimitMb: Math.max(64,  Math.min(1024,  Number(limits.memoryLimitMb)|| 256)),
      maxOutputBytes: MAX_OUTPUT_BYTES
    } : { maxOutputBytes: MAX_OUTPUT_BYTES };

    const res = await fetch(mode === "run" ? JUDGE_RUN_URL : JUDGE_URL, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(mode === "run" ? {
        lang,
        code,
        stdin: String(stdin ?? ""),
        limits: normalizedLimits
      } : {
        problemSlug: problem.slug,
        categorySlug: problem.categorySlug,
        lang,
        code,
        oracle: { lang: oracle.lang, code: oracle.code },
        limits: normalizedLimits
      })
    });
    const text = await res.text();
    return new NextResponse(text, {
      status: res.status,
      headers: { "content-type": res.headers.get("content-type") ?? "application/json" }
    });
  } catch (e: any) {
    return NextResponse.json(
      { status: "ERR", message: `judge unreachable: ${e?.message ?? e}` },
      { status: 502 }
    );
  }
}
