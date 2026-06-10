from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    grid = [list(map(int, line.split())) for line in lines[1:1 + n]]
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = grid[i][j] + max(dp[i - 1][j] if i else 0, dp[i][j - 1] if j else 0)
    return str(dp[n - 1][m - 1])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n7\n"),
        edge("1 4\n1 2 3 4\n"),
        edge("2 3\n1 2 3\n4 5 6\n"),
        edge("3 1\n1\n2\n3\n"),
        edge("3 3\n0 0 0\n0 0 0\n0 0 0\n"),
        stress("4 4\n1 0 2 3\n4 1 0 5\n2 2 2 2\n9 0 1 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
