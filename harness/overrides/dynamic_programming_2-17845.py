from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    n, k = tokens[0], tokens[1]
    idx = 2
    dp = [0] * (n + 1)
    for _ in range(k):
        value, time = tokens[idx], tokens[idx + 1]
        idx += 2
        for t in range(n, time - 1, -1):
            dp[t] = max(dp[t], dp[t - time] + value)
    return f"{dp[n]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("5 1\n10 6\n"),
        edge("10 3\n10 5\n40 4\n30 6\n"),
        edge("6 3\n10 3\n20 3\n25 6\n"),
        edge("4 4\n5 1\n6 1\n7 1\n8 1\n"),
        edge("10 2\n100 10\n99 9\n"),
        stress("15 5\n10 5\n12 6\n5 3\n30 8\n4 2\n"),
    ])
