export const MIN_TIME_LIMIT_MS = 1000;
export const MAX_TIME_LIMIT_MS = 10000;
export const DEFAULT_TIME_LIMIT_MS = 2000;

export const MIN_MEMORY_LIMIT_MB = 256;
export const MAX_MEMORY_LIMIT_MB = 1024;
export const DEFAULT_MEMORY_LIMIT_MB = 256;

export const DEFAULT_MAX_OUTPUT_BYTES = 64 * 1024 * 1024;

export type JudgeLimitInput = {
  timeLimitMs?: unknown;
  memoryLimitMb?: unknown;
  maxOutputBytes?: unknown;
};

export type NormalizedJudgeLimits = {
  timeLimitMs: number;
  memoryLimitMb: number;
  maxOutputBytes: number;
};

function positiveNumber(value: unknown): number | null {
  const n = Number(value);
  return Number.isFinite(n) && n > 0 ? n : null;
}

function clamp(value: number, low: number, high: number): number {
  return Math.max(low, Math.min(high, value));
}

export function normalizeJudgeLimits(limits?: JudgeLimitInput | null): NormalizedJudgeLimits {
  const time = positiveNumber(limits?.timeLimitMs) ?? DEFAULT_TIME_LIMIT_MS;
  const memory = positiveNumber(limits?.memoryLimitMb) ?? DEFAULT_MEMORY_LIMIT_MB;
  const output = positiveNumber(limits?.maxOutputBytes) ?? DEFAULT_MAX_OUTPUT_BYTES;

  return {
    timeLimitMs: Math.round(clamp(time, MIN_TIME_LIMIT_MS, MAX_TIME_LIMIT_MS)),
    memoryLimitMb: Math.round(clamp(memory, MIN_MEMORY_LIMIT_MB, MAX_MEMORY_LIMIT_MB)),
    maxOutputBytes: Math.round(output)
  };
}
