from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]
    vals = nums[1:]
    board = [vals[i * n:(i + 1) * n] for i in range(n)]
    counts = [0, 0]

    def rec(y: int, x: int, size: int) -> None:
        first = board[y][x]
        if all(board[i][j] == first for i in range(y, y + size) for j in range(x, x + size)):
            counts[first] += 1
            return
        h = size // 2
        rec(y, x, h); rec(y, x + h, h); rec(y + h, x, h); rec(y + h, x + h, h)

    rec(0, 0, n)
    return f"{counts[0]}\n{counts[1]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n0\n", "1\n1\n", "2\n0 0\n0 0\n", "2\n0 1\n1 0\n", "4\n1 1 0 0\n1 1 0 0\n0 0 1 1\n0 0 1 1\n", "4\n0 1 0 1\n1 0 1 0\n0 1 0 1\n1 0 1 0\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
