from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    coins = [1, 2, 5, 7]
    dp = [10**9] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("6\n"), stress("99\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
