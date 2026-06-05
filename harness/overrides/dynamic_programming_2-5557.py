from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n = values[0]
    numbers = values[1:1 + n]
    dp = [[0] * 21 for _ in range(n - 1)]
    dp[0][numbers[0]] = 1
    for i in range(1, n - 1):
        for current in range(21):
            if dp[i - 1][current] <= 0:
                continue
            for sign in (1, -1):
                nxt = current + sign * numbers[i]
                if 0 <= nxt < 21:
                    dp[i][nxt] += dp[i - 1][current]
    return f"{dp[n - 2][numbers[n - 1]]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("3\n1 1 2\n"),
        edge("3\n1 1 0\n"),
        edge("4\n1 2 3 0\n"),
        edge("5\n8 3 2 4 7\n"),
        edge("6\n1 1 1 1 1 3\n"),
        stress("11\n1 2 3 4 5 6 7 8 9 10 11\n"),
    ])
