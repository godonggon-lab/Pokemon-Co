from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    m = int(lines[1])
    parent = list(range(n + 2))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for line in lines[2:2 + m]:
        x, y = map(int, line.split())
        current = find(x)
        while current < y:
            parent[current] = find(current + 1)
            current = find(current)
    walls = sum(1 for i in range(1, n) if find(i) == i)
    return str(walls + 1)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n0\n"),
        edge("5\n0\n"),
        edge("5\n1\n2 4\n"),
        edge("5\n2\n1 2\n4 5\n"),
        edge("6\n2\n1 6\n2 5\n"),
        stress("8\n3\n1 3\n5 8\n2 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
