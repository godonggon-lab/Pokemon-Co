from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n = values[0]
    a = values[1:]
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n + 1):
        day = n - length + 1
        for left in range(n - length + 1):
            right = left + length - 1
            if left == right:
                dp[left][right] = day * a[left]
            else:
                dp[left][right] = max(dp[left + 1][right] + day * a[left], dp[left][right - 1] + day * a[right])
    return f"{dp[0][n - 1]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1\n5\n"),
        edge("3\n1\n2\n3\n"),
        edge("3\n3\n2\n1\n"),
        edge("4\n5\n5\n5\n5\n"),
        edge("5\n10\n1\n1\n1\n10\n"),
        stress("5\n4\n2\n7\n1\n5\n"),
    ])
