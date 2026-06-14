from __future__ import annotations

import itertools
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, _m, k = map(int, lines[0].split())
    origin = [list(map(int, lines[i].split())) for i in range(1, n + 1)]
    ops = [tuple(map(int, line.split())) for line in lines[n + 1 : n + 1 + k]]

    def rotate(arr: list[list[int]], op: tuple[int, int, int]) -> None:
        r, c, s = op
        r -= 1
        c -= 1
        for layer in range(1, s + 1):
            top, left = r - layer, c - layer
            bottom, right = r + layer, c + layer
            prev = arr[top][left]
            for i in range(top + 1, bottom + 1):
                arr[i][left], prev = prev, arr[i][left]
            for j in range(left + 1, right + 1):
                arr[bottom][j], prev = prev, arr[bottom][j]
            for i in range(bottom - 1, top - 1, -1):
                arr[i][right], prev = prev, arr[i][right]
            for j in range(right - 1, left - 1, -1):
                arr[top][j], prev = prev, arr[top][j]

    answer = 10**9
    for order in itertools.permutations(ops):
        arr = [row[:] for row in origin]
        for op in order:
            rotate(arr, op)
        answer = min(answer, min(sum(row) for row in arr))
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5 6 2\n1 2 3 2 5 6\n3 8 7 2 1 3\n8 2 3 1 4 5\n3 4 5 1 1 1\n9 3 2 1 4 3\n3 4 2\n4 2 1\n",
        "3 3 1\n1 2 3\n4 5 6\n7 8 9\n2 2 1\n",
        "4 4 2\n1 1 1 1\n2 2 2 2\n3 3 3 3\n4 4 4 4\n2 2 1\n3 3 1\n",
        "3 3 1\n1 1 1\n1 1 1\n1 1 1\n2 2 1\n",
        "5 5 2\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n3 3 2\n3 3 1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    grid = "\n".join(" ".join(str((i + j) % 9 + 1) for j in range(6)) for i in range(6))
    ops = "\n".join(["3 3 2", "4 4 2", "3 4 1"])
    hard = f"6 6 3\n{grid}\n{ops}\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
