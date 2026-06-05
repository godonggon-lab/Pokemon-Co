from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    h, n = map(int, data.split())
    if h > n:
        h, n = n, h
    size = n + 1
    dp = [[0] * size for _ in range(size)]
    dp[h][h] = 1
    for i in range(h, n + 1):
        for j in range(h, i + 1):
            if i == h and j == h:
                continue
            dp[i][j] = (dp[i - 1][j] if i > h else 0) + (dp[i][j - 1] if j > h else 0)
    return f"{dp[n][n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n"), edge("2 4\n"), stress("4 10\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
