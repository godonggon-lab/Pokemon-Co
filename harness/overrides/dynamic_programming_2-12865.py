from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, k = nums[:2]
    dp = [0] * (k + 1)
    idx = 2
    for _ in range(n):
        w, v = nums[idx], nums[idx + 1]
        idx += 2
        for cap in range(k, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return f"{dp[k]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 5\n6 10\n"),
        edge("4 7\n6 13\n4 8\n3 6\n5 12\n"),
        edge("3 10\n10 1\n6 100\n4 100\n"),
        edge("4 5\n1 10\n1 20\n1 30\n1 40\n"),
        edge("3 3\n3 5\n3 6\n3 7\n"),
        stress("6 15\n5 10\n4 7\n6 12\n3 5\n8 20\n2 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
