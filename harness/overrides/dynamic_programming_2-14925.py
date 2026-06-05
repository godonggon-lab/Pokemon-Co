from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n, m = map(int, lines[0].split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    ans = 0
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        for j, value in enumerate(row, 1):
            if value == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n0\n"),
        edge("3 4\n0 0 1 0\n0 0 0 0\n1 0 0 0\n"),
        stress("6 7\n0 0 0 0 1 0 0\n0 0 0 0 1 0 0\n0 0 0 0 0 0 0\n1 0 0 0 0 1 0\n0 0 0 0 0 0 0\n0 1 0 0 0 0 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
