from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n, k = map(int, data.split())
    mod = 1000000000
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        acc = 0
        for total in range(n + 1):
            acc = (acc + dp[i - 1][total]) % mod
            dp[i][total] = acc
    return f"{dp[k][n]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("0 1\n"), edge("1 1\n"), edge("2 2\n"), edge("20 2\n"), edge("20 20\n"), stress("200 200\n")])
