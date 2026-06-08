from __future__ import annotations
from itertools import permutations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, health, gain = map(int, lines[0].split())
    home = (-1, -1)
    milks = []
    for i, line in enumerate(lines[1:1 + n]):
        for j, value in enumerate(map(int, line.split())):
            if value == 1:
                home = (i, j)
            elif value == 2:
                milks.append((i, j))
    best = 0
    for order in permutations(milks):
        hp = health
        x, y = home
        count = 0
        for nx, ny in order:
            dist = abs(x - nx) + abs(y - ny)
            if hp < dist:
                break
            hp = hp - dist + gain
            x, y = nx, ny
            count += 1
            if hp >= abs(x - home[0]) + abs(y - home[1]):
                best = max(best, count)
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1 1\n1 2\n2 0\n"),
        edge("3 2 1\n1 0 0\n0 2 0\n0 0 0\n"),
        edge("3 1 5\n1 0 2\n0 0 0\n0 0 0\n"),
        edge("4 3 2\n1 0 2 0\n0 0 0 0\n2 0 0 2\n0 0 0 0\n"),
        edge("4 1 1\n1 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 2\n"),
        stress("5 4 3\n1 0 2 0 0\n0 0 0 2 0\n2 0 0 0 0\n0 2 0 0 2\n0 0 0 0 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
