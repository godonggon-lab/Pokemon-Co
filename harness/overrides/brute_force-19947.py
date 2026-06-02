from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    money, years = map(int, data.split())
    dp = [0] * (years + 1)
    dp[0] = money
    for year in range(1, years + 1):
        dp[year] = int(dp[year - 1] * 1.05)
        if year >= 3:
            dp[year] = max(dp[year], int(dp[year - 3] * 1.20))
        if year >= 5:
            dp[year] = max(dp[year], int(dp[year - 5] * 1.35))
    return str(dp[years])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("10000 1\n"), edge("10000 3\n"), stress("12345 10\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
