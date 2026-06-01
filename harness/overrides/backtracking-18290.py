from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m, k = map(int, lines[0].split())
    grid = [list(map(int, line.split())) for line in lines[1:1 + n]]
    used = [[False] * m for _ in range(n)]
    cells = [(i, j) for i in range(n) for j in range(m)]
    best = -10**18

    def ok(x: int, y: int) -> bool:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and used[nx][ny]:
                return False
        return True

    def dfs(index: int, count: int, total: int) -> None:
        nonlocal best
        if count == k:
            best = max(best, total)
            return
        if index == len(cells) or len(cells) - index < k - count:
            return
        x, y = cells[index]
        if ok(x, y):
            used[x][y] = True
            dfs(index + 1, count + 1, total + grid[x][y])
            used[x][y] = False
        dfs(index + 1, count, total)

    dfs(0, 0, 0)
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1 1\n7\n"),
        edge("2 2 2\n1 2\n3 4\n"),
        stress("4 4 4\n1 -2 3 4\n-5 6 -7 8\n9 -10 11 -12\n13 14 -15 16\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
