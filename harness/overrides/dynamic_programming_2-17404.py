from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n = int(lines[0])
    cost = [list(map(int, line.split())) for line in lines[1:]]
    inf = 10**15
    answer = inf
    for first in range(3):
        dp = [[inf] * 3 for _ in range(n)]
        dp[0][first] = cost[0][first]
        for i in range(1, n):
            for color in range(3):
                dp[i][color] = cost[i][color] + min(dp[i - 1][prev] for prev in range(3) if prev != color)
        for last in range(3):
            if last != first:
                answer = min(answer, dp[-1][last])
    return f"{answer}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("3\n26 40 83\n49 60 57\n13 89 99\n"),
        edge("4\n1 100 100\n100 1 100\n100 100 1\n1 100 100\n"),
        stress("5\n7 3 8\n2 9 4\n6 1 5\n8 7 2\n3 4 6\n"),
    ])
