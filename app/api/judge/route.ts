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
const MAX_CODE_BYTES = 64 * 1024;

// 사용자 제출 허용 언어는 python / cpp / java 로 통일.
// (oracle 코드는 어떤 언어든 사용 가능 — 출력만 같으면 되므로.)
const ALLOWED_LANGS = new Set([
  "python", "cpp", "java"
]);

export async function POST(req: Request) {
  let body: any;
  try { body = await req.json(); }
  catch { return NextResponse.json({ status: "ERR", message: "invalid json" }, { status: 400 }); }

  const { problemSlug, lang, code, limits } = body ?? {};
  if (typeof problemSlug !== "string" || typeof lang !== "string" || typeof code !== "string") {
    return NextResponse.json({ status: "ERR", message: "missing fields" }, { status: 400 });
  }
  if (!ALLOWED_LANGS.has(lang)) {
    return NextResponse.json({ status: "ERR", message: `lang not supported: ${lang}` }, { status: 400 });
  }
  if (Buffer.byteLength(code, "utf8") > MAX_CODE_BYTES) {
    return NextResponse.json({ status: "ERR", message: "code too large" }, { status: 413 });
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
    const res = await fetch(JUDGE_URL, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        problemSlug: problem.slug,
        categorySlug: problem.categorySlug,
        lang,
        code,
        oracle: { lang: oracle.lang, code: oracle.code },
        limits: (limits && typeof limits === "object") ? {
          timeLimitMs:  Math.max(500, Math.min(10000, Number(limits.timeLimitMs)  || 2000)),
          memoryLimitMb: Math.max(64,  Math.min(1024,  Number(limits.memoryLimitMb)|| 256))
        } : undefined
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
