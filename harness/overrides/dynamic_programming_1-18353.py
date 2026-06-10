from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    a = nums[1:]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] > a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return f"{n - max(dp)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("5\n5 4 3 2 1\n"),
        edge("5\n1 2 3 4 5\n"),
        edge("5\n3 3 3 3 3\n"),
        edge("6\n10 1 9 2 8 3\n"),
        stress("7\n15 11 4 8 5 2 4\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
