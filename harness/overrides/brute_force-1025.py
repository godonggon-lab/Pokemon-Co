from __future__ import annotations
import math
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    grid = lines[1:1 + n]
    answer = -1
    for sx in range(n):
        for sy in range(m):
            for dx in range(-n, n):
                for dy in range(-m, m):
                    if dx == 0 and dy == 0:
                        continue
                    x, y = sx, sy
                    current = ""
                    while 0 <= x < n and 0 <= y < m:
                        current += grid[x][y]
                        value = int(current)
                        root = math.isqrt(value)
                        if root * root == value:
                            answer = max(answer, value)
                        x += dx
                        y += dy
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n9\n"),
        edge("1 2\n16\n"),
        edge("2 2\n12\n34\n"),
        edge("3 3\n123\n456\n789\n"),
        edge("3 4\n0001\n2222\n3333\n"),
        stress("4 5\n00144\n62536\n98765\n43210\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
