from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    p, w = map(int, lines[0].split())
    c, v = map(int, lines[1].split())
    edges = [tuple(map(int, line.split())) for line in lines[2:2 + w]]
    parent = list(range(p))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b, width in sorted(edges, key=lambda item: -item[2]):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
        if find(c) == find(v):
            return str(width)
    return ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1\n0 1\n0 1 7\n"),
        edge("3 3\n0 2\n0 1 5\n1 2 4\n0 2 2\n"),
        edge("4 4\n0 3\n0 1 10\n1 3 3\n0 2 5\n2 3 4\n"),
        edge("4 5\n1 2\n0 1 8\n1 2 6\n0 2 3\n2 3 10\n1 3 4\n"),
        edge("5 4\n0 4\n0 1 9\n1 2 8\n2 3 7\n3 4 6\n"),
        stress("5 6\n1 4\n0 1 7\n1 2 6\n2 4 5\n1 3 4\n3 4 9\n0 4 2\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
