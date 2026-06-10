from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    grid = lines[1:1 + n]
    parent = list(range(n * m))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    for i in range(n):
        for j in range(m):
            di, dj = dirs[grid[i][j]]
            ni, nj = i + di, j + dj
            union(i * m + j, ni * m + nj)
    return str(len({find(i) for i in range(n * m)}))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\nU\n"),
        edge("2 2\nRD\nUL\n"),
        edge("2 2\nDD\nUU\n"),
        edge("2 3\nRDL\nRUL\n"),
        edge("3 3\nRDD\nURD\nUUL\n"),
        stress("3 4\nRRRD\nULLD\nUUUL\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
