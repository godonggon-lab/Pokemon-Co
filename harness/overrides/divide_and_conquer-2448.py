from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


REPLACE_SAMPLES = True


def expected(stdin: str) -> str:
    n = int(stdin)
    width = 2 * n - 1
    board = [[" "] * width for _ in range(n)]

    def draw(y: int, x: int, size: int) -> None:
        if size == 3:
            pattern = ["  *  ", " * * ", "*****"]
            for i, row in enumerate(pattern):
                for j, ch in enumerate(row):
                    board[y + i][x + j] = ch
            return
        half = size // 2
        draw(y, x + half, half)
        draw(y + half, x, half)
        draw(y + half, x + size, half)

    draw(0, 0, n)
    return "\n".join("".join(row) for row in board) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["3\n", "6\n", "12\n", "24\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
