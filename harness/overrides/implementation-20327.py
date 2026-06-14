from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, r = map(int, lines[0].split())
    size = 1 << n
    arr = [list(map(int, lines[i].split())) for i in range(1, size + 1)]
    commands = [tuple(map(int, line.split())) for line in lines[size + 1 : size + 1 + r]]

    def rotate_clock(block: list[list[int]]) -> list[list[int]]:
        return [list(row) for row in zip(*block[::-1])]

    def rotate_counter(block: list[list[int]]) -> list[list[int]]:
        return [list(row) for row in zip(*block)][::-1]

    def apply_inside(a: list[list[int]], level: int, op: int) -> list[list[int]]:
        block_size = 1 << level
        out = [row[:] for row in a]
        for sr in range(0, size, block_size):
            for sc in range(0, size, block_size):
                block = [row[sc : sc + block_size] for row in a[sr : sr + block_size]]
                if op == 1:
                    block = block[::-1]
                elif op == 2:
                    block = [row[::-1] for row in block]
                elif op == 3:
                    block = rotate_clock(block)
                elif op == 4:
                    block = rotate_counter(block)
                for i in range(block_size):
                    out[sr + i][sc : sc + block_size] = block[i]
        return out

    def apply_whole(a: list[list[int]], level: int, op: int) -> list[list[int]]:
        block_size = 1 << level
        count = size // block_size
        blocks = [[None] * count for _ in range(count)]
        for i in range(count):
            for j in range(count):
                blocks[i][j] = [row[j * block_size : (j + 1) * block_size] for row in a[i * block_size : (i + 1) * block_size]]
        if op == 5:
            blocks = blocks[::-1]
        elif op == 6:
            blocks = [row[::-1] for row in blocks]
        elif op == 7:
            blocks = [list(row) for row in zip(*blocks[::-1])]
        elif op == 8:
            blocks = [list(row) for row in zip(*blocks)][::-1]
        out = [[0] * size for _ in range(size)]
        for i in range(count):
            for j in range(count):
                for x in range(block_size):
                    out[i * block_size + x][j * block_size : (j + 1) * block_size] = blocks[i][j][x]
        return out

    for op, level in commands:
        arr = apply_inside(arr, level, op) if op <= 4 else apply_whole(arr, level, op)
    return "\n".join(" ".join(map(str, row)) for row in arr)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n1 1\n2 2\n7 1\n8 0\n",
        "1 3\n1 2\n3 4\n3 1\n4 1\n5 0\n",
        "3 2\n1 2 3 4 5 6 7 8\n9 10 11 12 13 14 15 16\n17 18 19 20 21 22 23 24\n25 26 27 28 29 30 31 32\n33 34 35 36 37 38 39 40\n41 42 43 44 45 46 47 48\n49 50 51 52 53 54 55 56\n57 58 59 60 61 62 63 64\n6 1\n7 2\n",
        "1 2\n1 2\n3 4\n1 0\n8 1\n",
        "2 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n5 1\n6 1\n7 1\n8 1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    size = 8
    grid = "\n".join(" ".join(str(i * size + j + 1) for j in range(size)) for i in range(size))
    commands = "\n".join(["1 1", "2 2", "3 1", "4 2", "5 1", "6 2", "7 1", "8 0"])
    hard = f"3 8\n{grid}\n{commands}\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
