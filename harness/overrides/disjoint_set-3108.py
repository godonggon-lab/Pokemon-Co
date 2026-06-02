from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _touches(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> bool:
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    if ax2 < bx1 or bx2 < ax1 or ay2 < by1 or by2 < ay1:
        return False
    if ax1 < bx1 and bx2 < ax2 and ay1 < by1 and by2 < ay2:
        return False
    if bx1 < ax1 and ax2 < bx2 and by1 < ay1 and ay2 < by2:
        return False
    return True


def _on_origin(rect: tuple[int, int, int, int]) -> bool:
    x1, y1, x2, y2 = rect
    return (x1 <= 0 <= x2 and (y1 == 0 or y2 == 0)) or (y1 <= 0 <= y2 and (x1 == 0 or x2 == 0))


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    rects = [tuple(map(int, line.split())) for line in lines[1:1 + n]]
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i in range(n):
        for j in range(i):
            if _touches(rects[i], rects[j]):
                union(i, j)
    components = len({find(i) for i in range(n)})
    return str(components - (1 if any(_on_origin(rect) for rect in rects) else 0))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 1 2 2\n"),
        edge("2\n-1 -1 1 1\n2 2 3 3\n"),
        stress("4\n-2 -2 2 2\n2 -1 4 1\n5 5 6 6\n-6 5 -5 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
