from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    v, e = map(int, lines[0].split())
    parent = list(range(v + 1))
    degree = [0] * (v + 1)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for line in lines[1:1 + e]:
        a, b = map(int, line.split())
        degree[a] += 1
        degree[b] += 1
        union(a, b)
    used = [i for i in range(1, v + 1) if degree[i] > 0]
    connected = not used or len({find(i) for i in used}) == 1
    odd = sum(value % 2 for value in degree)
    return "YES" if connected and odd in (0, 2) else "NO"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 0\n"),
        edge("3 2\n1 2\n2 3\n"),
        edge("4 2\n1 2\n3 4\n"),
        edge("3 3\n1 2\n2 3\n3 1\n"),
        edge("4 3\n1 2\n1 3\n1 4\n"),
        stress("5 5\n1 2\n2 3\n3 4\n4 5\n5 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
