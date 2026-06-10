from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    mod = 10007
    if n == 1:
        return "0\n"
    dp = [[0] * (n + 2) for _ in range(n + 1)]
    dp[2][1] = 2
    for i in range(3, n + 1):
        for d in range(1, i):
            dp[i][d] = (dp[i - 1][d] * 2 + dp[i - 1][d - 1] + dp[i - 1][d + 1]) % mod
    return f"{sum(dp[n][1:n]) % mod}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n"),
        edge("3\n"),
        edge("4\n"),
        edge("5\n"),
        edge("10\n"),
        stress("20\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
