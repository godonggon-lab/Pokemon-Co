from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n, m = map(int, lines[0].split())
    board = [list(map(int, line.split())) for line in lines[1:]]
    neg = -10**15
    dp = [[[neg] * m for _ in range(n)] for _ in range(2)]
    dp[0][n - 1][0] = board[n - 1][0]
    for y in range(n - 1, -1, -1):
        for x in range(m):
            if y + 1 < n:
                dp[0][y][x] = max(dp[0][y][x], dp[0][y + 1][x] + board[y][x])
            if x - 1 >= 0:
                dp[0][y][x] = max(dp[0][y][x], dp[0][y][x - 1] + board[y][x])
    dp[1][n - 1][m - 1] = board[n - 1][m - 1]
    for y in range(n - 1, -1, -1):
        for x in range(m - 1, -1, -1):
            if y + 1 < n:
                dp[1][y][x] = max(dp[1][y][x], dp[1][y + 1][x] + board[y][x])
            if x + 1 < m:
                dp[1][y][x] = max(dp[1][y][x], dp[1][y][x + 1] + board[y][x])
    answer = max(dp[0][y][x] + dp[1][y][x] for y in range(n) for x in range(m))
    return f"{answer}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1 1\n5\n"),
        edge("1 2\n1 2\n"),
        edge("2 1\n1\n2\n"),
        edge("2 2\n1 2\n3 4\n"),
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n"),
        stress("3 4\n1 -2 3 4\n5 6 -7 8\n9 10 11 -12\n"),
    ])
