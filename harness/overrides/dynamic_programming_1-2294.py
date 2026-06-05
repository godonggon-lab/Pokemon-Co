from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, k = nums[:2]
    coins = nums[2 : 2 + n]
    inf = 10**9
    dp = [inf] * (k + 1)
    dp[0] = 0
    for coin in coins:
        for value in range(coin, k + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)
    return f"{dp[k] if dp[k] < inf else -1}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n1\n"),
        edge("1 7\n3\n"),
        edge("3 15\n1\n5\n12\n"),
        edge("2 3\n2\n4\n"),
        edge("4 11\n1\n5\n5\n7\n"),
        stress("5 100\n1\n3\n7\n11\n50\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
