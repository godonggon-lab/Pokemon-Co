from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)
    dp = [0] + [4] * n
    for value in range(1, n + 1):
        root = int(value**0.5)
        for x in range(1, root + 1):
            dp[value] = min(dp[value], dp[value - x * x] + 1)
    return str(dp[n])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("2\n"),
        edge("3\n"),
        edge("4\n"),
        edge("999\n"),
        stress("5000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
