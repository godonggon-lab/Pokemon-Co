from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    grid = lines[1:1 + n]
    answer = 0
    for mask in range(1 << (n * m)):
        total = 0
        for i in range(n):
            current = 0
            for j in range(m):
                idx = i * m + j
                if mask & (1 << idx):
                    current = current * 10 + int(grid[i][j])
                else:
                    total += current
                    current = 0
            total += current
        for j in range(m):
            current = 0
            for i in range(n):
                idx = i * m + j
                if mask & (1 << idx):
                    total += current
                    current = 0
                else:
                    current = current * 10 + int(grid[i][j])
            total += current
        answer = max(answer, total)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n7\n"),
        edge("1 2\n12\n"),
        edge("2 1\n1\n2\n"),
        edge("2 3\n123\n456\n"),
        edge("2 2\n99\n99\n"),
        stress("3 3\n912\n345\n678\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
