from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n = values[0]
    arr = values[1:1 + n]
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return f"{n - max(dp)}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1\n1\n"),
        edge("7\n3\n7\n5\n2\n6\n1\n4\n"),
        edge("5\n1\n2\n3\n4\n5\n"),
        edge("5\n5\n4\n3\n2\n1\n"),
        edge("6\n2\n1\n4\n3\n6\n5\n"),
        stress("8\n8\n1\n7\n2\n6\n3\n5\n4\n"),
    ])
