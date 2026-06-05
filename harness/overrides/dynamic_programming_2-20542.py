from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n, m = map(int, lines[0].split())
    a = lines[1].strip()
    b = lines[2].strip()

    def same(x: str, y: str) -> bool:
        return x == y or (x in "ij" and y in "ij") or (x in "vl" and y in "vl")

    dp = [[10**9] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (0 if same(a[i - 1], b[j - 1]) else 1))
    return f"{dp[n][m]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("3 3\nabc\nabc\n"), edge("4 4\nilvj\njvli\n"), stress("5 6\nilabc\njlabbc\n")])
