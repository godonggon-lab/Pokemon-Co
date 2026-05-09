from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n, m, r = nums[0], nums[1], nums[2]
    vals = nums[3:]
    arr = [vals[i * m:(i + 1) * m] for i in range(n)]
    out = [row[:] for row in arr]
    layers = min(n, m) // 2
    for layer in range(layers):
        cells = []
        for x in range(layer, m - layer):
            cells.append((layer, x))
        for y in range(layer + 1, n - layer):
            cells.append((y, m - layer - 1))
        for x in range(m - layer - 2, layer - 1, -1):
            cells.append((n - layer - 1, x))
        for y in range(n - layer - 2, layer, -1):
            cells.append((y, layer))
        values = [arr[y][x] for y, x in cells]
        shift = r % len(values)
        rotated = values[shift:] + values[:shift]
        for (y, x), value in zip(cells, rotated):
            out[y][x] = value
    return "\n".join(" ".join(map(str, row)) for row in out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 2 1\n1 2\n3 4\n",
        "3 3 1\n1 2 3\n4 5 6\n7 8 9\n",
        "4 4 2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n",
        "2 4 3\n1 2 3 4\n5 6 7 8\n",
        "4 2 5\n1 2\n3 4\n5 6\n7 8\n",
        "6 6 7\n1 2 3 4 5 6\n7 8 9 10 11 12\n13 14 15 16 17 18\n19 20 21 22 23 24\n25 26 27 28 29 30\n31 32 33 34 35 36\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
