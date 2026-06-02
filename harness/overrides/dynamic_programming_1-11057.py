from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n = int(data)
    mod = 10007
    dp = [1] * 10
    for _ in range(2, n + 1):
        for i in range(1, 10):
            dp[i] = (dp[i] + dp[i - 1]) % mod
    return str(sum(dp) % mod)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("3\n"), stress("1000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
