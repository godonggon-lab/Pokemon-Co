from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    length = int(lines[0])
    positions = list(map(int, lines[2].split()))
    answer = max(positions[0], length - positions[-1])
    for left, right in zip(positions, positions[1:]):
        answer = max(answer, (right - left + 1) // 2)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("10\n1\n5\n"), edge("10\n2\n0 10\n"), stress("100\n5\n5 20 50 70 95\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
