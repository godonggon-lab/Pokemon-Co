from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    n, k = tokens[0], tokens[1]
    arr = tokens[2:2 + n]
    dp = [0] * (n + 1)
    left = 0
    total = 0
    for right, value in enumerate(arr, 1):
        total += value
        dp[right] = max(dp[right], dp[right - 1])
        while total >= k:
            dp[right] = max(dp[right], dp[left] + total - k)
            total -= arr[left]
            left += 1
    return f"{dp[n]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("5 5\n1 2 3 4 5\n"),
        edge("6 7\n2 2 2 2 2 2\n"),
        edge("1 10\n9\n"),
        edge("4 5\n5 5 5 5\n"),
        edge("7 8\n1 7 1 7 1 7 1\n"),
        stress("8 10\n5 1 3 7 2 6 4 8\n"),
    ])
