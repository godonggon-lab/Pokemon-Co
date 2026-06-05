from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)
    t = [0] * (n + 1)
    t[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            t[i] += t[j] * t[i - 1 - j]
    return str(t[n])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("0\n"),
        edge("1\n"),
        edge("2\n"),
        edge("3\n"),
        edge("10\n"),
        stress("35\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
