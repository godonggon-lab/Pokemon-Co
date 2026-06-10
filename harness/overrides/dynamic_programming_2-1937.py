from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n = int(lines[0])
    board = [list(map(int, line.split())) for line in lines[1:]]
    dp = [[0] * n for _ in range(n)]

    def dfs(x: int, y: int) -> int:
        if dp[x][y]:
            return dp[x][y]
        dp[x][y] = 1
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
        return dp[x][y]

    return f"{max(dfs(i, j) for i in range(n) for j in range(n))}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1\n7\n"),
        edge("2\n1 2\n4 3\n"),
        edge("3\n5 5 5\n5 5 5\n5 5 5\n"),
        edge("3\n1 2 3\n8 9 4\n7 6 5\n"),
        edge("4\n16 15 14 13\n5 6 7 12\n4 9 8 11\n3 2 1 10\n"),
        stress("4\n14 9 12 10\n1 11 5 4\n7 15 2 13\n6 3 16 8\n"),
    ])
