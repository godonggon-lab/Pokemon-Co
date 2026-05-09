from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]
    vals = nums[1:]
    board = [vals[i * n:(i + 1) * n] for i in range(n)]
    while n > 1:
        board = [[sorted([board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]])[2] for j in range(0, n, 2)] for i in range(0, n, 2)]
        n //= 2
    return f"{board[0][0]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["2\n1 2\n3 4\n", "2\n4 3\n2 1\n", "4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n", "4\n16 15 14 13\n12 11 10 9\n8 7 6 5\n4 3 2 1\n", "4\n1 100 2 99\n3 98 4 97\n5 96 6 95\n7 94 8 93\n", "8\n1 2 3 4 5 6 7 8\n9 10 11 12 13 14 15 16\n17 18 19 20 21 22 23 24\n25 26 27 28 29 30 31 32\n33 34 35 36 37 38 39 40\n41 42 43 44 45 46 47 48\n49 50 51 52 53 54 55 56\n57 58 59 60 61 62 63 64\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
