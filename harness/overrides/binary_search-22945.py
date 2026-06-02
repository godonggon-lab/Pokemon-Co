from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    abilities = list(map(int, lines[1].split()))
    left, right = 0, len(abilities) - 1
    answer = 0
    while left < right:
        answer = max(answer, (right - left - 1) * min(abilities[left], abilities[right]))
        if abilities[left] < abilities[right]:
            left += 1
        else:
            right -= 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("2\n1 2\n"), edge("5\n1 2 3 4 5\n"), stress("6\n6 1 5 2 4 3\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
