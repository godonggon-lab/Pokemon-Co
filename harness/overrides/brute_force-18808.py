from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _rotate(cells: list[tuple[int, int]], size: int) -> list[tuple[int, int]]:
    rotated = [(c, size - r - 1) for r, c in cells]
    min_r = min(r for r, _ in rotated)
    min_c = min(c for _, c in rotated)
    return [(r - min_r, c - min_c) for r, c in rotated]


def _place(n: int, m: int, cells: list[tuple[int, int]], occupied: set[tuple[int, int]]) -> set[tuple[int, int]] | None:
    for base_r in range(n):
        for base_c in range(m):
            pasted = set()
            ok = True
            for r, c in cells:
                nr, nc = base_r + r, base_c + c
                if nr >= n or nc >= m or (nr, nc) in occupied:
                    ok = False
                    break
                pasted.add((nr, nc))
            if ok:
                return pasted
    return None


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m, k = map(int, lines[0].split())
    cursor = 1
    stickers = []
    for _ in range(k):
        r, c = map(int, lines[cursor].split())
        cursor += 1
        cells = []
        for i in range(r):
            row = list(map(int, lines[cursor].split()))
            cursor += 1
            for j, value in enumerate(row):
                if value == 1:
                    cells.append((i, j))
        stickers.append([max(r, c), cells])
    occupied: set[tuple[int, int]] = set()
    queue = deque(stickers)
    rotations = 0
    while queue:
        if rotations == 4:
            queue.popleft()
            rotations = 0
            continue
        size, cells = queue.popleft()
        pasted = _place(n, m, cells, occupied)
        if pasted is not None:
            occupied.update(pasted)
            rotations = 0
        else:
            queue.appendleft((size, _rotate(cells, size)))
            rotations += 1
    return str(len(occupied))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1 1\n1 1\n1\n"),
        edge("2 2 1\n1 2\n1 1\n"),
        edge("3 3 2\n1 3\n1 1 1\n2 1\n1\n1\n"),
        edge("4 4 2\n2 2\n1 1\n1 1\n2 3\n1 0 1\n1 1 1\n"),
        edge("5 5 3\n2 3\n1 1 0\n0 1 1\n3 2\n1 0\n1 1\n0 1\n1 4\n1 1 1 1\n"),
        stress("6 6 4\n2 2\n1 1\n1 1\n2 3\n1 0 1\n1 1 1\n3 1\n1\n1\n1\n1 5\n1 1 1 1 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
