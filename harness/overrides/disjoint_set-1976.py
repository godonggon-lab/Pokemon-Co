from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    m = int(lines[1])
    parent = list(range(n + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i in range(1, n + 1):
        row = list(map(int, lines[1 + i].split()))
        for j, value in enumerate(row, start=1):
            if value:
                union(i, j)
    plan = list(map(int, lines[2 + n].split()))
    ok = all(find(plan[0]) == find(city) for city in plan[:m])
    return "YES" if ok else "NO"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n0\n1\n"),
        edge("2\n2\n0 1\n1 0\n1 2\n"),
        edge("3\n3\n0 1 0\n1 0 1\n0 1 0\n1 2 3\n"),
        edge("3\n2\n0 1 0\n1 0 0\n0 0 0\n1 3\n"),
        edge("5\n4\n0 1 0 0 0\n1 0 1 0 0\n0 1 0 1 0\n0 0 1 0 1\n0 0 0 1 0\n1 3 5 2\n"),
        stress("6\n5\n0 1 0 0 0 0\n1 0 1 0 0 0\n0 1 0 0 0 0\n0 0 0 0 1 0\n0 0 0 1 0 1\n0 0 0 0 1 0\n1 2 3 2 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
