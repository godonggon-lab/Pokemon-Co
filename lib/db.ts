// SQLite 데이터 액세스 (멀티유저).
//
// 테이블:
//   trainers   (id PK, name UNIQUE, tr, dex_count, created_at)
//   captures   (trainer_id, problem_slug, captured_at, attempts_at_capture, tr_at_capture, PK(trainer_id, problem_slug))
//   attempts   (trainer_id, problem_slug, count, PK(trainer_id, problem_slug))
//   history    (id PK, trainer_id, problem_slug, problem_r, expected, k, delta, prev_tr, next_tr, outcome, ts)
//   submissions(id PK, trainer_id, problem_slug, lang, status, passed, total, failed_case_kind, failed_case_verdict, duration_ms, code_hash, code_bytes, ts)
//
// 익명 세션: 트레이너 가입 시 랜덤 secret 발급 → httpOnly 쿠키 (dj_session = `${id}:${secret}`)
// 비밀번호 없는 프로토타입. 같은 기기/브라우저 = 같은 세션.

import Database from "better-sqlite3";
import path from "node:path";
import { mkdirSync } from "node:fs";
import crypto from "node:crypto";

const DATA_DIR = path.join(process.cwd(), ".data");
mkdirSync(DATA_DIR, { recursive: true });
const DB_PATH = path.join(DATA_DIR, "dongjun.db");

let _db: Database.Database | null = null;

function db(): Database.Database {
  if (_db) return _db;
  const d = new Database(DB_PATH);
  d.pragma("journal_mode = WAL");
  d.pragma("busy_timeout = 5000");
  d.pragma("foreign_keys = ON");
  d.exec(`
    CREATE TABLE IF NOT EXISTS trainers (
      id          INTEGER PRIMARY KEY AUTOINCREMENT,
      name        TEXT NOT NULL UNIQUE,
      secret      TEXT NOT NULL,
      tr          INTEGER NOT NULL DEFAULT 1000,
      dex_count   INTEGER NOT NULL DEFAULT 0,
      created_at  INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS captures (
      trainer_id          INTEGER NOT NULL REFERENCES trainers(id) ON DELETE CASCADE,
      problem_slug        TEXT    NOT NULL,
      captured_at         INTEGER NOT NULL,
      attempts_at_capture INTEGER NOT NULL,
      tr_at_capture       INTEGER NOT NULL,
      PRIMARY KEY (trainer_id, problem_slug)
    );

    CREATE TABLE IF NOT EXISTS attempts (
      trainer_id    INTEGER NOT NULL REFERENCES trainers(id) ON DELETE CASCADE,
      problem_slug  TEXT    NOT NULL,
      count         INTEGER NOT NULL DEFAULT 0,
      PRIMARY KEY (trainer_id, problem_slug)
    );

    CREATE TABLE IF NOT EXISTS history (
      id           INTEGER PRIMARY KEY AUTOINCREMENT,
      trainer_id   INTEGER NOT NULL REFERENCES trainers(id) ON DELETE CASCADE,
      problem_slug TEXT    NOT NULL,
      problem_r    INTEGER NOT NULL,
      expected     REAL    NOT NULL,
      k            INTEGER NOT NULL,
      delta        INTEGER NOT NULL,
      prev_tr      INTEGER NOT NULL,
      next_tr      INTEGER NOT NULL,
      outcome      TEXT    NOT NULL,  -- 'win' | 'loss'
      ts           INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS submissions (
      id                  INTEGER PRIMARY KEY AUTOINCREMENT,
      trainer_id          INTEGER REFERENCES trainers(id) ON DELETE SET NULL,
      problem_slug        TEXT    NOT NULL,
      lang                TEXT    NOT NULL,
      status              TEXT    NOT NULL,
      passed              INTEGER,
      total               INTEGER,
      failed_case_kind    TEXT,
      failed_case_verdict TEXT,
      duration_ms         INTEGER,
      code_hash           TEXT    NOT NULL,
      code_bytes          INTEGER NOT NULL,
      ts                  INTEGER NOT NULL
    );

    CREATE TABLE IF NOT EXISTS auth_accounts (
      id               INTEGER PRIMARY KEY AUTOINCREMENT,
      trainer_id       INTEGER NOT NULL REFERENCES trainers(id) ON DELETE CASCADE,
      provider         TEXT    NOT NULL,
      provider_user_id TEXT    NOT NULL,
      email            TEXT,
      display_name     TEXT,
      created_at       INTEGER NOT NULL,
      last_login_at    INTEGER NOT NULL,
      UNIQUE(provider, provider_user_id)
    );

    CREATE INDEX IF NOT EXISTS idx_history_trainer  ON history(trainer_id, ts DESC);
    CREATE INDEX IF NOT EXISTS idx_submissions_trainer ON submissions(trainer_id, ts DESC);
    CREATE INDEX IF NOT EXISTS idx_submissions_problem ON submissions(problem_slug, ts DESC);
    CREATE INDEX IF NOT EXISTS idx_trainers_tr      ON trainers(tr DESC);
    CREATE INDEX IF NOT EXISTS idx_auth_trainer     ON auth_accounts(trainer_id);
  `);
  _db = d;
  return d;
}

// ---------- 타입 ----------
export type DbTrainer = {
  id: number;
  name: string;
  tr: number;
  dexCount: number;
  createdAt: number;
};

export type DbCapture = {
  problemSlug: string;
  capturedAt: number;
  attemptsAtCapture: number;
  trAtCapture: number;
};

export type DbHistory = {
  id: number;
  problemSlug: string;
  problemR: number;
  expected: number;
  k: number;
  delta: number;
  prevTR: number;
  nextTR: number;
  outcome: "win" | "loss";
  ts: number;
};

export type RecordSubmissionArgs = {
  trainerId?: number | null;
  problemSlug: string;
  lang: string;
  status: string;
  passed?: number | null;
  total?: number | null;
  failedCaseKind?: string | null;
  failedCaseVerdict?: string | null;
  durationMs?: number | null;
  code: string;
};

export type AuthProvider = "kakao" | "naver";

export type DbAuthAccount = {
  provider: AuthProvider;
  providerUserId: string;
  email: string | null;
  displayName: string | null;
  createdAt: number;
  lastLoginAt: number;
};

// ---------- API ----------
export function createTrainer(name: string): { trainer: DbTrainer; secret: string } {
  const cleaned = name.trim().slice(0, 16);
  if (!cleaned) throw new Error("이름이 비어있어요");
  const secret = crypto.randomBytes(24).toString("hex");
  const now = Date.now();
  try {
    const info = db().prepare(
      "INSERT INTO trainers (name, secret, created_at) VALUES (?, ?, ?)"
    ).run(cleaned, secret, now);
    return {
      trainer: { id: Number(info.lastInsertRowid), name: cleaned, tr: 1000, dexCount: 0, createdAt: now },
      secret
    };
  } catch (e: any) {
    if (String(e?.message ?? "").includes("UNIQUE")) throw new Error("이미 존재하는 이름이에요");
    throw e;
  }
}

export function authenticate(id: number, secret: string): DbTrainer | null {
  const row = db().prepare("SELECT id, name, secret, tr, dex_count, created_at FROM trainers WHERE id = ?").get(id) as any;
  if (!row || row.secret !== secret) return null;
  return { id: row.id, name: row.name, tr: row.tr, dexCount: row.dex_count, createdAt: row.created_at };
}

export function getTrainerById(id: number): DbTrainer | null {
  const row = db().prepare("SELECT id, name, tr, dex_count, created_at FROM trainers WHERE id = ?").get(id) as any;
  return row ? { id: row.id, name: row.name, tr: row.tr, dexCount: row.dex_count, createdAt: row.created_at } : null;
}

export function findTrainerByAuthAccount(
  provider: AuthProvider,
  providerUserId: string
): { trainer: DbTrainer; secret: string } | null {
  const row = db().prepare(`
    SELECT t.id, t.name, t.secret, t.tr, t.dex_count, t.created_at
    FROM auth_accounts a
    JOIN trainers t ON t.id = a.trainer_id
    WHERE a.provider = ? AND a.provider_user_id = ?
  `).get(provider, providerUserId) as any;
  if (!row) return null;
  return {
    trainer: { id: row.id, name: row.name, tr: row.tr, dexCount: row.dex_count, createdAt: row.created_at },
    secret: row.secret
  };
}

export function linkAuthAccount(args: {
  trainerId: number;
  provider: AuthProvider;
  providerUserId: string;
  email?: string | null;
  displayName?: string | null;
}) {
  const now = Date.now();
  db().prepare(`
    INSERT INTO auth_accounts (
      trainer_id, provider, provider_user_id, email, display_name, created_at, last_login_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(provider, provider_user_id) DO UPDATE SET
      last_login_at = excluded.last_login_at,
      email = COALESCE(excluded.email, auth_accounts.email),
      display_name = COALESCE(excluded.display_name, auth_accounts.display_name)
  `).run(
    args.trainerId,
    args.provider,
    args.providerUserId,
    args.email ?? null,
    args.displayName ?? null,
    now,
    now
  );
}

export function listAuthAccounts(trainerId: number): DbAuthAccount[] {
  const rows = db().prepare(`
    SELECT provider, provider_user_id, email, display_name, created_at, last_login_at
    FROM auth_accounts
    WHERE trainer_id = ?
    ORDER BY created_at ASC
  `).all(trainerId) as any[];
  return rows.map((r) => ({
    provider: r.provider,
    providerUserId: r.provider_user_id,
    email: r.email,
    displayName: r.display_name,
    createdAt: r.created_at,
    lastLoginAt: r.last_login_at
  }));
}

export function listCaptures(trainerId: number): DbCapture[] {
  return (db().prepare(
    "SELECT problem_slug, captured_at, attempts_at_capture, tr_at_capture FROM captures WHERE trainer_id = ?"
  ).all(trainerId) as any[]).map(r => ({
    problemSlug: r.problem_slug,
    capturedAt: r.captured_at,
    attemptsAtCapture: r.attempts_at_capture,
    trAtCapture: r.tr_at_capture
  }));
}

export function listAttempts(trainerId: number): Record<string, number> {
  const rows = db().prepare("SELECT problem_slug, count FROM attempts WHERE trainer_id = ?").all(trainerId) as any[];
  const out: Record<string, number> = {};
  for (const r of rows) out[r.problem_slug] = r.count;
  return out;
}

export function bumpAttempt(trainerId: number, slug: string) {
  db().prepare(`
    INSERT INTO attempts (trainer_id, problem_slug, count) VALUES (?, ?, 1)
    ON CONFLICT(trainer_id, problem_slug) DO UPDATE SET count = count + 1
  `).run(trainerId, slug);
}

export type ApplyOutcomeArgs = {
  problemSlug: string;
  problemR: number;
  expected: number;
  k: number;
  delta: number;       // applyOutcome().delta
  prevTR: number;
  nextTR: number;
  outcome: "win" | "loss";
};

export function applyWin(trainerId: number, args: ApplyOutcomeArgs): { firstCapture: boolean } {
  const now = Date.now();
  return db().transaction(() => {
    db().prepare("UPDATE trainers SET tr = ? WHERE id = ?").run(args.nextTR, trainerId);
    const had = db().prepare("SELECT 1 FROM captures WHERE trainer_id = ? AND problem_slug = ?")
      .get(trainerId, args.problemSlug);
    if (!had) {
      const att = db().prepare("SELECT count FROM attempts WHERE trainer_id = ? AND problem_slug = ?")
        .get(trainerId, args.problemSlug) as any;
      db().prepare(`
        INSERT INTO captures (trainer_id, problem_slug, captured_at, attempts_at_capture, tr_at_capture)
        VALUES (?, ?, ?, ?, ?)
      `).run(trainerId, args.problemSlug, now, att?.count ?? 1, args.nextTR);
      db().prepare("UPDATE trainers SET dex_count = dex_count + 1 WHERE id = ?").run(trainerId);
    }
    insertHistory(trainerId, args, now);
    return { firstCapture: !had };
  })();
}

export function applyLoss(trainerId: number, args: ApplyOutcomeArgs) {
  const now = Date.now();
  db().transaction(() => {
    db().prepare("UPDATE trainers SET tr = ? WHERE id = ?").run(args.nextTR, trainerId);
    insertHistory(trainerId, args, now);
  })();
}

function insertHistory(trainerId: number, a: ApplyOutcomeArgs, now: number) {
  db().prepare(`
    INSERT INTO history (trainer_id, problem_slug, problem_r, expected, k, delta, prev_tr, next_tr, outcome, ts)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).run(trainerId, a.problemSlug, a.problemR, a.expected, a.k, a.delta, a.prevTR, a.nextTR, a.outcome, now);
}

export function leaderboardTop(limit = 50): { id: number; name: string; tr: number; dexCount: number }[] {
  const rows = db().prepare(
    "SELECT id, name, tr, dex_count FROM trainers ORDER BY tr DESC LIMIT ?"
  ).all(limit) as any[];
  return rows.map(r => ({ id: r.id, name: r.name, tr: r.tr, dexCount: r.dex_count }));
}

export function recentHistory(trainerId: number, limit = 20): DbHistory[] {
  return (db().prepare(`
    SELECT id, problem_slug, problem_r, expected, k, delta, prev_tr, next_tr, outcome, ts
    FROM history WHERE trainer_id = ? ORDER BY ts DESC LIMIT ?
  `).all(trainerId, limit) as any[]).map(r => ({
    id: r.id, problemSlug: r.problem_slug, problemR: r.problem_r,
    expected: r.expected, k: r.k, delta: r.delta,
    prevTR: r.prev_tr, nextTR: r.next_tr, outcome: r.outcome, ts: r.ts
  }));
}

export function recordSubmission(args: RecordSubmissionArgs) {
  const codeBytes = Buffer.byteLength(args.code, "utf8");
  const codeHash = crypto.createHash("sha256").update(args.code).digest("hex");
  db().prepare(`
    INSERT INTO submissions (
      trainer_id, problem_slug, lang, status, passed, total,
      failed_case_kind, failed_case_verdict, duration_ms, code_hash, code_bytes, ts
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).run(
    args.trainerId ?? null,
    args.problemSlug,
    args.lang,
    args.status,
    args.passed ?? null,
    args.total ?? null,
    args.failedCaseKind ?? null,
    args.failedCaseVerdict ?? null,
    args.durationMs ?? null,
    codeHash,
    codeBytes,
    Date.now()
  );
}
