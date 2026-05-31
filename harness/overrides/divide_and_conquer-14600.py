from __future__ import annotations
from collections import defaultdict
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 1\n"), edge("2\n2 3\n"), stress("2\n4 4\n")]

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
