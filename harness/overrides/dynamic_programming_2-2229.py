from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n = values[0]
    arr = [0] + values[1:1 + n]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        mn = mx = arr[i]
        for j in range(i, 0, -1):
            mn = min(mn, arr[j])
            mx = max(mx, arr[j])
            dp[i] = max(dp[i], dp[j - 1] + mx - mn)
    return f"{dp[n]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1\n7\n"), edge("4\n1 5 2 4\n"), stress("6\n10 1 7 3 9 2\n")])
