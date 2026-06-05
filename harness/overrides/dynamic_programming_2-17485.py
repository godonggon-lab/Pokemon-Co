from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n, m = map(int, lines[0].split())
    board = [list(map(int, line.split())) for line in lines[1:]]
    inf = 10**12
    dp = [[[inf] * m for _ in range(n)] for _ in range(3)]
    for j in range(m):
        for direction in range(3):
            dp[direction][0][j] = board[0][j]
    for i in range(1, n):
        for j in range(m):
            dp[0][i][j] = min(dp[1][i - 1][j], dp[2][i - 1][j]) + board[i][j]
            if j != m - 1:
                dp[1][i][j] = min(dp[0][i - 1][j + 1], dp[2][i - 1][j + 1]) + board[i][j]
            if j != 0:
                dp[2][i][j] = min(dp[0][i - 1][j - 1], dp[1][i - 1][j - 1]) + board[i][j]
    return f"{min(min(dp[0][-1]), min(dp[1][-1]), min(dp[2][-1]))}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("2 2\n1 2\n3 4\n"),
        edge("3 3\n1 100 1\n1 100 1\n1 1 1\n"),
        edge("3 4\n5 8 5 1\n3 2 4 7\n9 1 3 2\n"),
        edge("4 3\n1 2 3\n4 5 6\n7 8 9\n1 1 1\n"),
        edge("5 5\n9 9 9 9 9\n1 9 1 9 1\n9 1 9 1 9\n1 9 1 9 1\n9 9 9 9 9\n"),
        stress("6 6\n" + "\n".join(" ".join(str((i * 5 + j * 7) % 20 + 1) for j in range(6)) for i in range(6)) + "\n"),
    ])
