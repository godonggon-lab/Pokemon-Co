from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n, k = map(int, data.split())
    return str(max(int(str(n * i)[::-1]) for i in range(1, k + 1)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n"),
        edge("12 5\n"),
        edge("10 10\n"),
        edge("97 9\n"),
        edge("123 20\n"),
        stress("999 100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
