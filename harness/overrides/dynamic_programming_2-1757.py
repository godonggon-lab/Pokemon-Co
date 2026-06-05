from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    n, m = tokens[0], tokens[1]
    distance = tokens[2:]
    neg = -10**15
    dp = [[neg] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for tired in range(m + 1):
            if dp[i][tired] == neg:
                continue
            if tired == 0:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])
            else:
                dp[i + 1][tired - 1] = max(dp[i + 1][tired - 1], dp[i][tired])
            if tired < m:
                dp[i + 1][tired + 1] = max(dp[i + 1][tired + 1], dp[i][tired] + distance[i])
    return f"{dp[n][0]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1 1\n5\n"), edge("3 1\n5\n10\n20\n"), stress("6 2\n3\n8\n4\n7\n6\n5\n")])
