from __future__ import annotations
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    colors = [tuple(map(int, line.split())) for line in lines[1:1 + n]]
    target = tuple(map(int, lines[1 + n].split()))
    best = 10**9
    for count in range(2, min(7, n) + 1):
        for selected in combinations(colors, count):
            average = tuple(sum(color[i] for color in selected) // count for i in range(3))
            best = min(best, sum(abs(average[i] - target[i]) for i in range(3)))
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n0 0 0\n255 255 255\n128 128 128\n"),
        edge("3\n255 0 0\n0 255 0\n0 0 255\n128 128 128\n"),
        edge("3\n10 10 10\n10 10 10\n10 10 10\n10 10 10\n"),
        edge("4\n10 20 30\n40 50 60\n70 80 90\n100 110 120\n50 60 70\n"),
        edge("4\n0 0 0\n255 0 0\n0 255 0\n0 0 255\n85 85 85\n"),
        stress("5\n0 0 0\n255 255 255\n120 80 40\n40 80 120\n200 100 50\n100 100 100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
