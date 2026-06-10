from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    idx = 0
    n = values[idx]
    idx += 1
    weights = values[idx:idx + n]
    idx += n
    m = values[idx]
    idx += 1
    balls = values[idx:idx + m]
    possible = {0}
    for weight in weights:
        next_possible = set(possible)
        for value in possible:
            next_possible.add(abs(value - weight))
            next_possible.add(value + weight)
        possible = next_possible
    return " ".join("Y" if ball in possible else "N" for ball in balls) + "\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("2\n1 4\n4\n3 2 5 6\n"),
        edge("1\n7\n3\n7 14 1\n"),
        edge("1\n1\n3\n0 1 2\n"),
        edge("3\n1 1 1\n5\n1 2 3 4 5\n"),
        edge("4\n2 3 7 11\n5\n1 5 9 18 23\n"),
        stress("5\n1 3 9 27 81\n6\n1 2 4 40 121 122\n"),
    ])
