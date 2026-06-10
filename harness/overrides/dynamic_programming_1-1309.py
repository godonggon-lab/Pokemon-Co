from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)
    empty = left = right = 1
    for _ in range(2, n + 1):
        empty, left, right = (empty + left + right) % 9901, (empty + right) % 9901, (empty + left) % 9901
    return str((empty + left + right) % 9901)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("2\n"),
        edge("3\n"),
        edge("10\n"),
        edge("100\n"),
        stress("1000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
