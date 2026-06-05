from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    import sys

    sys.setrecursionlimit(10000)
    nums = list(map(int, data.split()))
    n, m = nums[:2]
    grid = [nums[2 + i * m : 2 + (i + 1) * m] for i in range(n)]
    memo = [[-1] * m for _ in range(n)]

    def dfs(r: int, c: int) -> int:
        if r == n - 1 and c == m - 1:
            return 1
        if memo[r][c] != -1:
            return memo[r][c]
        total = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[r][c] > grid[nr][nc]:
                total += dfs(nr, nc)
        memo[r][c] = total
        return total

    return f"{dfs(0, 0)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n7\n"),
        edge("1 3\n3 2 1\n"),
        edge("3 1\n3\n2\n1\n"),
        edge("2 2\n4 3\n2 1\n"),
        edge("3 3\n9 6 3\n8 5 2\n7 4 1\n"),
        stress("5 5\n25 24 23 22 21\n20 19 18 17 16\n15 14 13 12 11\n10 9 8 7 6\n5 4 3 2 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
