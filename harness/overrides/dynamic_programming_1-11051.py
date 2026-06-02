from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n, k = map(int, data.split())
    mod = 10007
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
        if i <= k:
            dp[i][i] = 1
    for i in range(2, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
    return str(dp[n][k])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("5 2\n"), edge("10 0\n"), edge("10 10\n"), edge("100 50\n"), stress("1000 500\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
