from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    n, target = map(int, stdin.split())
    board = [[0] * n for _ in range(n)]
    y = x = d = 0
    pos = (0, 0)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for num in range(n * n, 0, -1):
        board[y][x] = num
        if num == target:
            pos = (y, x)
        ny, nx = y + dirs[d][0], x + dirs[d][1]
        if not (0 <= ny < n and 0 <= nx < n) or board[ny][nx] != 0:
            d = (d + 1) % 4
            ny, nx = y + dirs[d][0], x + dirs[d][1]
        y, x = ny, nx
    return "".join(" ".join(map(str, row)) + "\n" for row in board) + f"{pos[0] + 1} {pos[1] + 1}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["3 5\n", "5 1\n", "5 25\n", "7 49\n", "7 13\n", "9 81\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
