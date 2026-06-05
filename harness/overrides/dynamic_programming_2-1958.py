from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    a, b, c = data.strip().splitlines()
    dp = [[[0] * (len(c) + 1) for _ in range(len(b) + 1)] for __ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    return f"{dp[-1][-1][-1]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("abc\nabc\nabc\n"), edge("abc\ndef\nghi\n"), stress("abcdxyz\nabxycdz\nzzabcdx\n")])
