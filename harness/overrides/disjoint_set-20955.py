from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    parent = list(range(n + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    cycle = 0
    for line in lines[1:1 + m]:
        a, b = map(int, line.split())
        ra, rb = find(a), find(b)
        if ra == rb:
            cycle += 1
        else:
            parent[rb] = ra
    components = len({find(i) for i in range(1, n + 1)})
    return str(cycle + components - 1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 2\n1 2\n2 3\n"),
        edge("4 4\n1 2\n2 3\n3 1\n3 4\n"),
        stress("6 5\n1 2\n2 3\n4 5\n5 6\n6 4\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
