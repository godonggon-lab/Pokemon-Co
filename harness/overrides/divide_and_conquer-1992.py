from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    board = lines[1:]

    def rec(y: int, x: int, size: int) -> str:
        first = board[y][x]
        if all(board[i][j] == first for i in range(y, y + size) for j in range(x, x + size)):
            return first
        h = size // 2
        return "(" + rec(y, x, h) + rec(y, x + h, h) + rec(y + h, x, h) + rec(y + h, x + h, h) + ")"

    return rec(0, 0, n) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n0\n", "2\n00\n00\n", "2\n01\n10\n", "4\n0000\n0011\n0011\n1111\n", "4\n1111\n1001\n1001\n1111\n", "8\n11110000\n11110000\n00011100\n00011100\n11110000\n11110000\n11110011\n11110011\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
