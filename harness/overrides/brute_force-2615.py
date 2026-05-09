from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    board = [list(map(int, line.split())) for line in stdin.strip().splitlines()]
    dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    for y in range(19):
        for x in range(19):
            color = board[y][x]
            if color == 0:
                continue
            for dy, dx in dirs:
                py, px = y - dy, x - dx
                if 0 <= py < 19 and 0 <= px < 19 and board[py][px] == color:
                    continue
                cells = [(y + dy * k, x + dx * k) for k in range(5)]
                if all(0 <= cy < 19 and 0 <= cx < 19 and board[cy][cx] == color for cy, cx in cells):
                    ny, nx = y + dy * 5, x + dx * 5
                    if not (0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == color):
                        return f"{color}\n{y + 1} {x + 1}\n"
    return "0\n"


def board(stones: list[tuple[int, int, int]]) -> str:
    grid = [[0] * 19 for _ in range(19)]
    for y, x, c in stones:
        grid[y - 1][x - 1] = c
    return "\n".join(" ".join(map(str, row)) for row in grid) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        board([]),
        board([(1, i, 1) for i in range(1, 6)]),
        board([(i, 1, 2) for i in range(1, 7)]),
        board([(i, i, 1) for i in range(3, 8)]),
        board([(10 - i, i, 2) for i in range(1, 6)]),
        board([(5, i, 1) for i in range(5, 10)] + [(1, 1, 2), (2, 2, 2)]),
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
