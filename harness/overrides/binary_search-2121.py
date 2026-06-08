from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    width, height = map(int, lines[1].split())
    points = [tuple(map(int, line.split())) for line in lines[2:2 + n]]
    point_set = set(points)
    answer = 0
    for x, y in points:
        if (x + width, y) in point_set and (x, y + height) in point_set and (x + width, y + height) in point_set:
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("4\n1 1\n0 0\n1 0\n0 1\n1 1\n"),
        edge("3\n2 2\n0 0\n2 0\n0 2\n"),
        edge("5\n2 2\n0 0\n2 0\n0 2\n2 2\n4 4\n"),
        edge("6\n1 2\n0 0\n1 0\n0 2\n1 2\n2 2\n2 0\n"),
        edge("4\n10 10\n0 0\n10 0\n0 10\n5 5\n"),
        stress("7\n2 3\n0 0\n2 0\n0 3\n2 3\n4 3\n4 0\n9 9\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
