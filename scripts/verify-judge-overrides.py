from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from harness.judge_core import DockerRunner, LocalRunner, judge


def main() -> int:
    problems = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    extra_path = ROOT / "data" / "problems-extra.json"
    if extra_path.exists():
        problems.extend(json.loads(extra_path.read_text(encoding="utf-8")))
    override_dir = ROOT / "harness" / "overrides"
    override_slugs = sorted(path.stem for path in override_dir.glob("*.py") if path.name != "__init__.py")

    if len(sys.argv) > 1:
        requested = set(sys.argv[1:])
        override_slugs = [slug for slug in override_slugs if slug in requested]

    by_slug = {problem["slug"]: problem for problem in problems}
    local = LocalRunner()
    docker = DockerRunner()
    failures: list[str] = []

    for slug in override_slugs:
        problem = by_slug.get(slug)
        if problem is None:
            failures.append(f"{slug}: problem metadata not found")
            continue

        sources = problem.get("sources") or []
        source = next((item for item in sources if item.get("lang") == "python"), sources[0] if sources else None)
        if source is None:
            failures.append(f"{slug}: oracle source not found")
            continue

        lang = source["lang"]
        user_runner = docker if lang in {"cpp", "java"} else local
        result = judge(
            problem_slug=slug,
            category_slug=problem["categorySlug"],
            user_lang=lang,
            user_code=source["code"],
            oracle_lang=lang,
            oracle_code=source["code"],
            user_runner=user_runner,
            oracle_runner=local,
            time_limit_s=4.0,
            case_count=6,
        )

        status = result.get("status")
        passed = result.get("passed")
        total = result.get("total")
        message = result.get("message", "")
        print(f"{slug:<42} {lang:<6} {status:<3} {passed}/{total} {message}")
        if status != "AC":
            failures.append(f"{slug}: {status} {message}")

    if failures:
        print("\nFailures:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"\nOK: {len(override_slugs)} override files self-judged successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
