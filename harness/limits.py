from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

MIN_TIME_LIMIT_MS = 1000
MAX_TIME_LIMIT_MS = 10000
DEFAULT_TIME_LIMIT_MS = 2000

# Docker executes compilation inside the same container. A BOJ 128 MB style
# runtime limit can falsely kill g++/javac during compile, so the local judge
# uses a safer floor while still preserving larger problem limits.
MIN_MEMORY_LIMIT_MB = 256
MAX_MEMORY_LIMIT_MB = 1024
DEFAULT_MEMORY_LIMIT_MB = 256

DEFAULT_MAX_OUTPUT_BYTES = 64 * 1024 * 1024


@dataclass(frozen=True)
class JudgeLimits:
    time_limit_s: float
    time_limit_ms: int
    memory_limit_mb: int
    max_output_bytes: int
    raw_time_limit_ms: int | None
    raw_memory_limit_mb: int | None
    source: str

    def as_payload(self) -> dict[str, Any]:
        return asdict(self)


def _problem_id_from_slug(problem_slug: str | None) -> str | None:
    if not problem_slug:
        return None
    tail = problem_slug.rsplit("-", 1)[-1]
    return tail if tail.isdigit() else None


def _coerce_positive_int(value: Any) -> int | None:
    try:
        n = int(float(value))
    except (TypeError, ValueError):
        return None
    return n if n > 0 else None


def _load_statement_limits(problem_slug: str | None) -> tuple[int | None, int | None]:
    problem_id = _problem_id_from_slug(problem_slug)
    if not problem_id:
        return None, None

    path = Path(__file__).resolve().parent.parent / "data" / "problems-statements.json"
    if not path.exists():
        return None, None

    try:
        statements = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None, None

    statement = statements.get(problem_id)
    if not isinstance(statement, dict) or statement.get("_failed"):
        return None, None

    limits = statement.get("limits")
    if not isinstance(limits, dict):
        return None, None

    return (
        _coerce_positive_int(limits.get("timeLimitMs")),
        _coerce_positive_int(limits.get("memoryLimitMb")),
    )


def _clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


def resolve_limits(
    problem_slug: str | None = None,
    requested: dict[str, Any] | None = None,
    *,
    default_max_output_bytes: int = DEFAULT_MAX_OUTPUT_BYTES,
) -> JudgeLimits:
    requested = requested if isinstance(requested, dict) else {}

    requested_time = _coerce_positive_int(requested.get("timeLimitMs"))
    requested_memory = _coerce_positive_int(requested.get("memoryLimitMb"))
    statement_time, statement_memory = _load_statement_limits(problem_slug)

    raw_time = requested_time or statement_time
    raw_memory = requested_memory or statement_memory
    source = "requested" if requested_time or requested_memory else "statement"
    if raw_time is None and raw_memory is None:
        source = "fallback"

    time_limit_ms = _clamp(
        raw_time or DEFAULT_TIME_LIMIT_MS,
        MIN_TIME_LIMIT_MS,
        MAX_TIME_LIMIT_MS,
    )
    memory_limit_mb = _clamp(
        raw_memory or DEFAULT_MEMORY_LIMIT_MB,
        MIN_MEMORY_LIMIT_MB,
        MAX_MEMORY_LIMIT_MB,
    )

    max_output_bytes = _coerce_positive_int(requested.get("maxOutputBytes"))
    if max_output_bytes is None:
        max_output_bytes = default_max_output_bytes

    return JudgeLimits(
        time_limit_s=time_limit_ms / 1000,
        time_limit_ms=time_limit_ms,
        memory_limit_mb=memory_limit_mb,
        max_output_bytes=max_output_bytes,
        raw_time_limit_ms=raw_time,
        raw_memory_limit_mb=raw_memory,
        source=source,
    )
