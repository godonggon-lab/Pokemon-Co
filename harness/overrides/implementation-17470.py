from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, _m, _r = map(int, lines[0].split())
    arr = [list(map(int, lines[i].split())) for i in range(1, n + 1)]
    ops = list(map(int, lines[n + 1].split()))

    def split(a: list[list[int]]) -> list[list[list[int]]]:
        h, w = len(a) // 2, len(a[0]) // 2
        return [
            [row[:w] for row in a[:h]],
            [row[w:] for row in a[:h]],
            [row[:w] for row in a[h:]],
            [row[w:] for row in a[h:]],
        ]

    def merge(parts: list[list[list[int]]]) -> list[list[int]]:
        top = [parts[0][i] + parts[1][i] for i in range(len(parts[0]))]
        bottom = [parts[2][i] + parts[3][i] for i in range(len(parts[2]))]
        return top + bottom

    for op in ops:
        if op == 1:
            arr = arr[::-1]
        elif op == 2:
            arr = [row[::-1] for row in arr]
        elif op == 3:
            arr = [list(row) for row in zip(*arr[::-1])]
        elif op == 4:
            arr = [list(row) for row in zip(*arr)][::-1]
        else:
            p = split(arr)
            arr = merge([p[2], p[0], p[3], p[1]] if op == 5 else [p[1], p[3], p[0], p[2]])
    return "\n".join(" ".join(map(str, row)) for row in arr)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "6 8 6\n3 2 6 3 1 2 9 7\n9 7 8 2 1 4 5 3\n5 9 2 1 9 6 1 8\n2 1 3 8 6 3 9 2\n1 3 2 8 7 9 2 1\n4 5 1 9 8 2 1 3\n1 2 3 4 5 6\n",
        "2 2 4\n1 2\n3 4\n1 2 5 6\n",
        "4 6 3\n1 2 3 4 5 6\n7 8 9 10 11 12\n13 14 15 16 17 18\n19 20 21 22 23 24\n3 5 4\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    grid = "\n".join(" ".join(str(i * 8 + j + 1) for j in range(8)) for i in range(8))
    hard = f"8 8 12\n{grid}\n1 2 3 4 5 6 1 2 3 4 5 6\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
