from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m, q = map(int, lines[0].split())
    edges = [None] + [tuple(map(int, line.split())) for line in lines[1:1 + m]]
    removed = [int(line) for line in lines[1 + m:1 + m + q]]
    removed_set = set(removed)
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> int:
        ra, rb = find(a), find(b)
        if ra == rb:
            return 0
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        cost = size[ra] * size[rb]
        parent[rb] = ra
        size[ra] += size[rb]
        return cost

    for i in range(1, m + 1):
        if i not in removed_set:
            union(*edges[i])
    answer = 0
    for index in reversed(removed):
        answer += union(*edges[index])
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 2 1\n1 2\n2 3\n1\n"),
        edge("4 3 2\n1 2\n2 3\n3 4\n1\n3\n"),
        stress("5 5 3\n1 2\n2 3\n3 4\n4 5\n1 5\n2\n4\n5\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
