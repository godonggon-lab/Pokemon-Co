from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    n = int(stdin)
    size = 4 * (n - 1) + 1
    board = [[" "] * size for _ in range(size)]
    for k in range(0, size // 2 + 1, 2):
        last = size - k - 1
        for i in range(k, last + 1):
            board[k][i] = board[last][i] = board[i][k] = board[i][last] = "*"
    return "\n".join("".join(row) for row in board) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n", "3\n", "4\n", "5\n", "10\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
