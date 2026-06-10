from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    it = iter(data.split())
    n, m, k = int(next(it)), int(next(it)), int(next(it))
    dp = [[0] * (k + 1) for _ in range(m + 1)]
    for _ in range(n):
        burger, fries = int(next(it)), int(next(it))
        for i in range(m, burger - 1, -1):
            for j in range(k, fries - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - burger][j - fries] + 1)
    return f"{dp[m][k]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1 1 1\n1 1\n"),
        edge("3 5 5\n3 3\n2 2\n5 5\n"),
        edge("3 2 2\n3 1\n1 3\n2 2\n"),
        edge("4 4 4\n2 2\n2 2\n2 2\n2 2\n"),
        edge("5 6 3\n1 1\n2 1\n3 1\n4 2\n2 3\n"),
        stress("5 10 10\n3 4\n4 3\n2 5\n5 2\n6 6\n"),
    ])
