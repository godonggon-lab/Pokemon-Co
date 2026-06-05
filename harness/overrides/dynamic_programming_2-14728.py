from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, t = nums[:2]
    dp = [0] * (t + 1)
    idx = 2
    for _ in range(n):
        k, score = nums[idx], nums[idx + 1]
        idx += 2
        for time in range(t, k - 1, -1):
            dp[time] = max(dp[time], dp[time - k] + score)
    return f"{dp[t]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 5\n6 10\n"), edge("3 10\n5 10\n4 40\n6 30\n"), stress("5 15\n5 10\n6 12\n3 5\n8 30\n2 4\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
