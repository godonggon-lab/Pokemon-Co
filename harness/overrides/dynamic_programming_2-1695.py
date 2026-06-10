from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    a = nums[1:]
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            if a[left] == a[right]:
                dp[left][right] = dp[left + 1][right - 1] if left + 1 <= right - 1 else 0
            else:
                dp[left][right] = min(dp[left + 1][right], dp[left][right - 1]) + 1
    return f"{dp[0][n - 1]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("5\n1 2 3 2 1\n"),
        edge("4\n1 2 3 4\n"),
        edge("6\n1 1 1 1 1 1\n"),
        edge("6\n1 2 3 1 2 3\n"),
        stress("8\n1 3 2 4 2 3 1 5\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
