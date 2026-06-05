from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    d, p = tokens[0], tokens[1]
    idx = 2
    dp = [0] * (d + 1)
    dp[0] = 10**9
    for _ in range(p):
        length, capacity = tokens[idx], tokens[idx + 1]
        idx += 2
        for x in range(d, length - 1, -1):
            dp[x] = max(dp[x], min(dp[x - length], capacity))
    return f"{dp[d]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("5 1\n5 7\n"), edge("10 3\n5 5\n5 9\n10 3\n"), stress("15 5\n5 10\n4 8\n6 7\n10 6\n1 100\n")])
