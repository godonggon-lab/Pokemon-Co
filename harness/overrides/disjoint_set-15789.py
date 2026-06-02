from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]

    for line in lines[1:1 + m]:
        a, b = map(int, line.split())
        union(a, b)
    c, h, k = map(int, lines[1 + m].split())
    root = find(c)
    enemy = find(h)
    others = sorted((size[find(i)] for i in range(1, n + 1) if find(i) == i and find(i) not in (root, enemy)), reverse=True)
    return str(size[root] + sum(others[:k]))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("3 1\n1 2\n1 3 0\n"), stress("8 3\n1 2\n3 4\n5 6\n1 7 2\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
