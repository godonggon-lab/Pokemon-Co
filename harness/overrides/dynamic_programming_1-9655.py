from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    return "SK\n" if n % 2 else "CY\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("2\n"),
        edge("3\n"),
        edge("4\n"),
        edge("999\n"),
        stress("1000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
