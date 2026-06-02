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

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    out = []
    for line in lines[1:1 + m]:
        op, a, b = map(int, line.split())
        if op == 0:
            union(a, b)
        else:
            out.append("YES" if find(a) == find(b) else "NO")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n1 1 1\n"),
        edge("3 4\n0 1 2\n1 1 2\n1 2 3\n0 2 3\n"),
        edge("5 6\n0 1 2\n0 3 4\n1 1 3\n0 2 3\n1 1 4\n1 4 5\n"),
        edge("7 8\n0 1 2\n0 2 3\n1 1 3\n1 1 4\n0 4 5\n0 5 6\n0 6 7\n1 4 7\n"),
        edge("10 7\n1 1 10\n0 1 10\n1 1 10\n0 2 9\n0 9 10\n1 2 1\n1 3 4\n"),
        stress("12 12\n0 1 2\n0 2 3\n0 4 5\n0 5 6\n1 1 6\n0 3 4\n1 1 6\n0 7 8\n0 8 9\n0 9 10\n0 10 11\n1 7 11\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
