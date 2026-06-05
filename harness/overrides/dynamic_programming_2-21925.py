from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n = values[0]
    arr = values[1:1 + n]
    pal = [[False] * n for _ in range(n)]
    for left in range(n):
        for right in range(left, n):
            if (right - left + 1) % 2 == 0 and arr[left:right + 1] == arr[left:right + 1][::-1]:
                pal[left][right] = True
    dp = [-10**9] * (n + 1)
    dp[0] = 0
    for i in range(n):
        if dp[i] < 0:
            continue
        for j in range(i + 1, n, 2):
            if pal[i][j]:
                dp[j + 1] = max(dp[j + 1], dp[i] + 1)
    return f"{dp[n] if dp[n] >= 0 else -1}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("2\n1 1\n"), edge("4\n1 2 2 1\n"), stress("6\n1 2 1 1 2 1\n")])
