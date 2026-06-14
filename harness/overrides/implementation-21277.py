from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n1, m1 = map(int, lines[0].split())
    a = lines[1 : 1 + n1]
    pos = 1 + n1
    n2, m2 = map(int, lines[pos].split())
    b = lines[pos + 1 : pos + 1 + n2]

    def cells(grid: list[str]) -> list[tuple[int, int]]:
        return [(i, j) for i, row in enumerate(grid) for j, ch in enumerate(row) if ch == "1"]

    def rotate(grid: list[str]) -> list[str]:
        return ["".join(row) for row in zip(*grid[::-1])]

    base = cells(a)
    answer = 10**9
    for _ in range(4):
        other = cells(b)
        for dr in range(-len(b), len(a) + 1):
            for dc in range(-len(b[0]), len(a[0]) + 1):
                moved = [(r + dr, c + dc) for r, c in other]
                if set(base) & set(moved):
                    continue
                all_cells = base + moved
                min_r = min(r for r, _ in all_cells)
                max_r = max(r for r, _ in all_cells)
                min_c = min(c for _, c in all_cells)
                max_c = max(c for _, c in all_cells)
                answer = min(answer, (max_r - min_r + 1) * (max_c - min_c + 1))
        b = rotate(b)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 2\n10\n11\n2 2\n01\n11\n",
        "1 3\n111\n1 2\n11\n",
        "3 3\n010\n111\n010\n2 2\n10\n11\n",
        "1 1\n1\n1 1\n1\n",
        "1 2\n11\n2 1\n1\n1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "4 5\n10101\n01110\n11100\n00111\n3 4\n1101\n0111\n1010\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
