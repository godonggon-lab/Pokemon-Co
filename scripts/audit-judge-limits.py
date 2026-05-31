from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from harness.limits import MIN_MEMORY_LIMIT_MB, resolve_limits


def load_problem_slugs() -> list[str]:
    slugs: list[str] = []
    for name in ("problems.json", "problems-extra.json"):
        path = ROOT / "data" / name
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for problem in data:
            slug = problem.get("slug")
            if isinstance(slug, str):
                slugs.append(slug)
    return sorted(set(slugs))


def main() -> int:
    slugs = load_problem_slugs()
    fallback = 0
    normalized_memory = 0
    min_time_ms = None
    max_time_ms = None

    for slug in slugs:
        limits = resolve_limits(slug)
        if limits.source == "fallback":
            fallback += 1
        if (
            limits.raw_memory_limit_mb is not None
            and limits.raw_memory_limit_mb < MIN_MEMORY_LIMIT_MB
            and limits.memory_limit_mb == MIN_MEMORY_LIMIT_MB
        ):
            normalized_memory += 1
        min_time_ms = limits.time_limit_ms if min_time_ms is None else min(min_time_ms, limits.time_limit_ms)
        max_time_ms = limits.time_limit_ms if max_time_ms is None else max(max_time_ms, limits.time_limit_ms)

    print(json.dumps({
        "totalProblems": len(slugs),
        "fallbackLimits": fallback,
        "memoryFlooredForDockerCompile": normalized_memory,
        "minTimeLimitMs": min_time_ms,
        "maxTimeLimitMs": max_time_ms,
        "ok": True,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
