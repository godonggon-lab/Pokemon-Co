from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    grid = lines[1:1 + n]
    state = [[0] * m for _ in range(n)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def dfs(x: int, y: int) -> int:
        if not (0 <= x < n and 0 <= y < m):
            return 2
        if state[x][y]:
            return state[x][y]
        state[x][y] = 1
        dx, dy = dirs[grid[x][y]]
        result = dfs(x + dx, y + dy)
        state[x][y] = 2 if result == 2 else 3
        return state[x][y]

    return str(sum(1 for i in range(n) for j in range(m) if dfs(i, j) == 2))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\nU\n"),
        edge("1 3\nRRR\n"),
        edge("2 2\nRD\nUL\n"),
        edge("2 2\nUU\nDD\n"),
        edge("3 3\nRRD\nULL\nUUU\n"),
        stress("3 4\nRRRD\nULLD\nUUUL\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
