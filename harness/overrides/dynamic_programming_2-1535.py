from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    hp = nums[1 : 1 + n]
    joy = nums[1 + n : 1 + 2 * n]
    dp = [0] * 100
    for h, j in zip(hp, joy):
        for value in range(99, h - 1, -1):
            dp[value] = max(dp[value], dp[value - h] + j)
    return f"{max(dp)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n1 21 79\n20 30 25\n"),
        edge("4\n20 30 40 50\n20 30 40 50\n"),
        edge("1\n99\n100\n"),
        edge("2\n50 50\n100 1000\n"),
        edge("5\n10 10 10 10 60\n1 2 3 4 100\n"),
        stress("5\n10 20 30 40 50\n5 20 30 40 100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
