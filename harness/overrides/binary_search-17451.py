from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    values = list(map(int, lines[1].split()))
    speed = 0
    for value in reversed(values):
        if speed <= value:
            speed = value
        else:
            speed = ((speed + value - 1) // value) * value
    return str(speed)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n7\n"), edge("3\n3 2 5\n"), stress("5\n4 6 8 3 7\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
