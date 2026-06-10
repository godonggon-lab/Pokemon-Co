from __future__ import annotations
from collections import defaultdict
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 1\n"),
        edge("2\n1 1\n"),
        edge("2\n4 4\n"),
        edge("3\n1 1\n"),
        edge("3\n5 6\n"),
        stress("4\n9 8\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]

def _solve(data: str) -> str:
    k, x, y = map(int, data.split())
    n = 2 ** k
    board = [[0] * n for _ in range(n)]
    hole = (n - y, x - 1)
    board[hole[0]][hole[1]] = -1
    tile = 0

    def cover(r: int, c: int, size: int, hr: int, hc: int) -> None:
        nonlocal tile
        if size == 1:
            return
        half = size // 2
        tile += 1
        current = tile
        mids = [
            (r + half - 1, c + half - 1),
            (r + half - 1, c + half),
            (r + half, c + half - 1),
            (r + half, c + half),
        ]
        quadrant = (0 if hr < r + half else 2) + (0 if hc < c + half else 1)
        for i, (mr, mc) in enumerate(mids):
            if i != quadrant:
                board[mr][mc] = current
        holes = mids[:]
        holes[quadrant] = (hr, hc)
        cover(r, c, half, *holes[0])
        cover(r, c + half, half, *holes[1])
        cover(r + half, c, half, *holes[2])
        cover(r + half, c + half, half, *holes[3])

    cover(0, 0, n, *hole)
    return "\n".join(" ".join(map(str, row)) for row in board)

def check_output(stdin: str, _expected: str, actual: str) -> bool:
    return _check_tromino(stdin, actual)

def _check_tromino(stdin: str, actual: str) -> bool:
    data = list(map(int, stdin.split()))
    k, x, y = data
    n = 2 ** k
    rows = [line.split() for line in actual.strip().splitlines()]
    if len(rows) != n or any(len(row) != n for row in rows):
        return False
    try:
        board = [list(map(int, row)) for row in rows]
    except ValueError:
        return False
    drain = (n - y, x - 1)
    if board[drain[0]][drain[1]] != -1:
        return False
    tiles: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for r in range(n):
        for c in range(n):
            v = board[r][c]
            if (r, c) == drain:
                continue
            if v <= 0:
                return False
            tiles[v].append((r, c))
    for cells in tiles.values():
        if len(cells) != 3:
            return False
        rs = {r for r, _ in cells}
        cs = {c for _, c in cells}
        if len(rs) != 2 or len(cs) != 2:
            return False
    return sum(len(cells) for cells in tiles.values()) == n * n - 1
