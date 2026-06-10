from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for turn, line in enumerate(lines[1:1 + m], start=1):
        a, b = map(int, line.split())
        ra, rb = find(a), find(b)
        if ra == rb:
            return str(turn)
        parent[rb] = ra
    return "0"

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1\n0 1\n"),
        edge("3 2\n0 1\n1 2\n"),
        edge("3 3\n0 1\n1 2\n2 0\n"),
        edge("4 4\n0 1\n2 3\n1 2\n0 3\n"),
        edge("5 4\n0 1\n1 2\n2 3\n3 4\n"),
        stress("5 5\n0 1\n1 2\n3 4\n2 3\n4 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
