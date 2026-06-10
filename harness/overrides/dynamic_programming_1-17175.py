from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    mod = 1_000_000_007
    dp = [0] * max(3, n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + 1) % mod
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("0\n"), edge("1\n"), edge("2\n"), edge("5\n"), edge("10\n"), stress("50\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
