from __future__ import annotations
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _fits(h: int, w: int, first: tuple[int, int], second: tuple[int, int]) -> bool:
    a, b = first
    c, d = second
    return (max(a, c) <= h and b + d <= w) or (a + c <= h and max(b, d) <= w)

def _solve(data: str) -> str:
    lines = data.splitlines()
    h, w = map(int, lines[0].split())
    n = int(lines[1])
    stickers = [tuple(map(int, line.split())) for line in lines[2:2 + n]]
    answer = 0
    for first, second in combinations(stickers, 2):
        rotations1 = {first, (first[1], first[0])}
        rotations2 = {second, (second[1], second[0])}
        if any(_fits(h, w, r1, r2) for r1 in rotations1 for r2 in rotations2):
            answer = max(answer, first[0] * first[1] + second[0] * second[1])
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5 5\n2\n2 3\n3 2\n"),
        edge("2 2\n2\n2 2\n2 2\n"),
        edge("4 4\n3\n1 4\n4 1\n2 2\n"),
        edge("3 5\n3\n3 3\n2 3\n1 5\n"),
        edge("10 10\n2\n10 5\n5 10\n"),
        stress("10 8\n4\n3 4\n5 2\n8 1\n6 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
