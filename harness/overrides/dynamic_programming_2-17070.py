from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    grid = [nums[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1
    for i in range(n):
        for j in range(2, n):
            if grid[i][j]:
                continue
            dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][2]
            if i > 0:
                dp[i][j][1] += dp[i - 1][j][1] + dp[i - 1][j][2]
            if i > 0 and grid[i - 1][j] == 0 and grid[i][j - 1] == 0:
                dp[i][j][2] += sum(dp[i - 1][j - 1])
    return f"{sum(dp[n - 1][n - 1])}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n0 0 0\n0 0 0\n0 0 0\n"),
        edge("4\n0 0 0 0\n0 1 0 0\n0 0 0 0\n0 0 0 0\n"),
        stress("6\n0 0 0 0 0 0\n0 0 1 0 0 0\n0 0 0 0 1 0\n0 1 0 0 0 0\n0 0 0 1 0 0\n0 0 0 0 0 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
