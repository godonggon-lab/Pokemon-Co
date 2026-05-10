from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
OVERRIDES = ROOT / "harness" / "overrides"
sys.path.insert(0, str(ROOT))


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(f"quality_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def score(row: dict[str, Any]) -> tuple[int, list[str]]:
    points = 0
    gaps: list[str] = []
    if row["caseCount"] >= 6:
        points += 25
    else:
        gaps.append("case_count_lt_6")
    if row["edgeCount"] > 0:
        points += 20
    else:
        gaps.append("missing_edge")
    if row["stressCount"] > 0:
        points += 25
    else:
        gaps.append("missing_stress")
    if row["expectedCount"] == row["caseCount"]:
        points += 20
    else:
        gaps.append("some_cases_need_oracle")
    if row["replaceSamples"]:
        points += 5
    if row["caseCount"] >= 8:
        points += 5
    return min(points, 100), gaps


def main() -> int:
    problems = json.loads((ROOT / "data" / "problems.json").read_text(encoding="utf-8"))
    rows = []
    for problem in problems:
        path = OVERRIDES / f"{problem['slug']}.py"
        if not path.exists():
            rows.append({
                "slug": problem["slug"],
                "category": problem["categorySlug"],
                "caseCount": 0,
                "edgeCount": 0,
                "stressCount": 0,
                "fuzzCount": 0,
                "expectedCount": 0,
                "replaceSamples": False,
                "qualityScore": 0,
                "gaps": ["missing_override"],
            })
            continue
        module = load_module(path)
        cases = list(module.gen_inputs(0))
        kinds = [case.get("kind", "fuzz") if isinstance(case, dict) else "fuzz" for case in cases]
        row = {
            "slug": problem["slug"],
            "category": problem["categorySlug"],
            "caseCount": len(cases),
            "edgeCount": kinds.count("edge"),
            "stressCount": kinds.count("stress"),
            "fuzzCount": kinds.count("fuzz"),
            "expectedCount": sum(1 for case in cases if isinstance(case, dict) and isinstance(case.get("expected"), str)),
            "replaceSamples": bool(getattr(module, "REPLACE_SAMPLES", False)),
        }
        row["qualityScore"], row["gaps"] = score(row)
        rows.append(row)

    low = sorted(
        [row for row in rows if row["qualityScore"] < 70],
        key=lambda row: (row["qualityScore"], row["caseCount"], row["slug"]),
    )
    summary = {
        "total": len(rows),
        "averageQualityScore": round(sum(row["qualityScore"] for row in rows) / len(rows), 2),
        "lowQualityCount": len(low),
        "missingStressCount": sum(1 for row in rows if "missing_stress" in row["gaps"]),
        "allHaveOverride": all(row["caseCount"] > 0 for row in rows),
        "topLowQuality": low[:50],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
