from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)

    def digit_sum(value: int) -> int:
        return sum(map(int, str(value)))

    return str(sum(1 for value in range(1, n + 1) if value % digit_sum(value) == 0))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("20\n"), edge("1729\n"), stress("10000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
