from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    p = [0] + nums[1:]
    dp = [10**9] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[i - j] + p[j] for j in range(1, i + 1))
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n"),
        edge("2\n1 100\n"),
        edge("4\n1 5 6 7\n"),
        edge("5\n10 9 8 7 6\n"),
        edge("6\n6 5 4 3 2 1\n"),
        stress("100\n" + " ".join(str((i*13)%100+1) for i in range(1,101)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
