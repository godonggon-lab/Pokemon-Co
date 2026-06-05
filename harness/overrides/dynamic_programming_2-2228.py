from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n, m = values[0], values[1]
    arr = [0] + values[2:2 + n]
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i]
    neg = -10**15
    dp = [[neg] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            for k in range(1, i + 1):
                prev = 0 if k <= 2 and j == 1 else (dp[k - 2][j - 1] if k >= 2 else neg)
                if prev != neg:
                    dp[i][j] = max(dp[i][j], prev + prefix[i] - prefix[k - 1])
    return f"{dp[n][m]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1 1\n5\n"), edge("5 2\n1\n2\n-10\n3\n4\n"), stress("7 3\n5\n-1\n4\n-2\n3\n-10\n8\n")])
