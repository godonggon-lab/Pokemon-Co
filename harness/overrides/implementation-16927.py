from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m, r = map(int, lines[0].split())
    arr = [list(map(int, line.split())) for line in lines[1 : 1 + n]]
    for layer in range(min(n, m) // 2):
        positions: list[tuple[int, int]] = []
        for c in range(layer, m - layer):
            positions.append((layer, c))
        for row in range(layer + 1, n - layer):
            positions.append((row, m - layer - 1))
        for c in range(m - layer - 2, layer - 1, -1):
            positions.append((n - layer - 1, c))
        for row in range(n - layer - 2, layer, -1):
            positions.append((row, layer))
        values = [arr[row][col] for row, col in positions]
        shift = r % len(values)
        for idx, (row, col) in enumerate(positions):
            arr[row][col] = values[(idx + shift) % len(values)]
    return "\n".join(" ".join(map(str, row)) for row in arr)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 2 1\n1 2\n3 4\n",
        "4 4 2\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n",
        "3 5 7\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n",
        "2 4 0\n1 2 3 4\n5 6 7 8\n",
        "4 6 16\n1 2 3 4 5 6\n7 8 9 10 11 12\n13 14 15 16 17 18\n19 20 21 22 23 24\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    row = 1
    matrix = []
    for _ in range(10):
        matrix.append(" ".join(str(x) for x in range(row, row + 10)))
        row += 10
    stdin = "10 10 12345\n" + "\n".join(matrix) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
