from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    a = nums[1:]
    dp = a[:]
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])
    return f"{max(dp)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("5\n1\n2\n3\n4\n5\n"),
        edge("5\n5\n4\n3\n2\n1\n"),
        edge("5\n3\n3\n3\n3\n3\n"),
        edge("6\n1\n10\n2\n9\n3\n8\n"),
        stress("7\n3\n1\n5\n2\n6\n4\n7\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
