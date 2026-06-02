from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    cost = [list(map(int, line.split())) for line in lines[1:1 + n]]
    inf = 10**9
    dp = [[[inf] * 3 for _ in range(m)] for _ in range(n)]
    for col in range(m):
        for direction in range(3):
            dp[0][col][direction] = cost[0][col]
    offsets = (-1, 0, 1)
    for row in range(1, n):
        for col in range(m):
            for direction, offset in enumerate(offsets):
                prev_col = col - offset
                if 0 <= prev_col < m:
                    dp[row][col][direction] = cost[row][col] + min(
                        dp[row - 1][prev_col][prev_direction]
                        for prev_direction in range(3)
                        if prev_direction != direction
                    )
    return str(min(min(values) for values in dp[-1]))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 2\n1 2\n3 4\n"),
        edge("3 3\n1 9 1\n9 1 9\n1 9 1\n"),
        stress("5 4\n5 8 5 1\n3 2 7 6\n9 1 4 8\n2 6 3 5\n7 4 2 9\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
