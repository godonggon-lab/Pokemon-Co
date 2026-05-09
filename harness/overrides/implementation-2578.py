from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    board = [nums[i * 5:(i + 1) * 5] for i in range(5)]
    calls = nums[25:]
    marked = [[False] * 5 for _ in range(5)]

    def count_lines() -> int:
        rows = sum(all(row) for row in marked)
        cols = sum(all(marked[r][c] for r in range(5)) for c in range(5))
        diag = all(marked[i][i] for i in range(5)) + all(marked[i][4 - i] for i in range(5))
        return rows + cols + diag

    for turn, call in enumerate(calls, 1):
        for y in range(5):
            for x in range(5):
                if board[y][x] == call:
                    marked[y][x] = True
        if count_lines() >= 3:
            return f"{turn}\n"
    return "25\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    base = "1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n"
    inputs = [
        base + "1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n",
        base + "1 6 11 16 21\n2 7 12 17 22\n3 8 13 18 23\n4 9 14 19 24\n5 10 15 20 25\n",
        base + "1 7 13 19 25\n5 9 17 21 2\n3 4 6 8 10\n11 12 14 15 16\n18 20 22 23 24\n",
        base + "25 24 23 22 21\n20 19 18 17 16\n15 14 13 12 11\n10 9 8 7 6\n5 4 3 2 1\n",
        base + "13 1 5 21 25\n2 3 4 6 7\n8 9 10 11 12\n14 15 16 17 18\n19 20 22 23 24\n",
        base + "1 2 6 7 11\n12 16 17 21 22\n3 4 5 8 9\n10 13 14 15 18\n19 20 23 24 25\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
