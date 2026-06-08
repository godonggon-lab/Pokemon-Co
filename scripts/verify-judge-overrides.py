from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from harness.judge_core import DockerRunner, LocalRunner, judge


def _parse_shard(value: str) -> tuple[int, int]:
    try:
        index_text, total_text = value.split("/", 1)
        index = int(index_text)
        total = int(total_text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("shard must use the form INDEX/TOTAL, for example 1/8") from exc

    if total < 1:
        raise argparse.ArgumentTypeError("shard total must be greater than 0")
    if index < 1 or index > total:
        raise argparse.ArgumentTypeError("shard index must be between 1 and total")
    return index, total


def _select_shard(slugs: list[str], shard: tuple[int, int] | None) -> list[str]:
    if shard is None:
        return slugs
    index, total = shard
    offset = index - 1
    return [slug for pos, slug in enumerate(slugs) if pos % total == offset]


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Self-judge override files with their reference solution.")
    parser.add_argument("slugs", nargs="*", help="Optional override slugs to verify.")
    parser.add_argument(
        "--shard",
        type=_parse_shard,
        help="Verify only one deterministic shard, using INDEX/TOTAL such as 1/8.",
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="Print the selected override slugs without running the judge.",
    )
    return parser.parse_args(argv)


def main() -> int:
    args = _parse_args(sys.argv[1:])
    problems = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    extra_path = ROOT / "data" / "problems-extra.json"
    if extra_path.exists():
        problems.extend(json.loads(extra_path.read_text(encoding="utf-8")))
    override_dir = ROOT / "harness" / "overrides"
    override_slugs = sorted(path.stem for path in override_dir.glob("*.py") if path.name != "__init__.py")

    if args.slugs:
        requested = set(args.slugs)
        override_slugs = [slug for slug in override_slugs if slug in requested]
    override_slugs = _select_shard(override_slugs, args.shard)

    if args.list_only:
        for slug in override_slugs:
            print(slug)
        print(f"\nSelected {len(override_slugs)} override files.")
        return 0

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
