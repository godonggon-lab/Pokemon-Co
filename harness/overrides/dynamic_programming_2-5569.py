from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    w, h = map(int, data.split())
    mod = 100000
    dp = [[[[0] * 2 for _ in range(2)] for __ in range(w + 1)] for ___ in range(h + 1)]
    for x in range(2, w + 1):
        dp[1][x][0][0] = 1
    for y in range(2, h + 1):
        dp[y][1][1][0] = 1
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if y == 1 or x == 1:
                continue
            dp[y][x][0][0] = (dp[y][x - 1][0][0] + dp[y][x - 1][0][1]) % mod
            dp[y][x][0][1] = dp[y][x - 1][1][0]
            dp[y][x][1][0] = (dp[y - 1][x][1][0] + dp[y - 1][x][1][1]) % mod
            dp[y][x][1][1] = dp[y - 1][x][0][0]
    return f"{sum(dp[h][w][direction][turn] for direction in range(2) for turn in range(2)) % mod}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("2 2\n"), edge("4 3\n"), stress("7 6\n")])
