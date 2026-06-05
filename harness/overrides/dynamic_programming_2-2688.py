from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    dp = [[0] * 10 for _ in range(65)]
    for digit in range(10):
        dp[1][digit] = 1
    for length in range(2, 65):
        for digit in range(10):
            dp[length][digit] = sum(dp[length - 1][digit:])
    values = list(map(int, data.split()))
    t = values[0]
    return "\n".join(str(sum(dp[n])) for n in values[1:1 + t]) + "\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("3\n1\n2\n3\n"), edge("4\n10\n20\n30\n64\n"), stress("10\n" + "\n".join(str(i * 6 + 1) for i in range(10)) + "\n")])
