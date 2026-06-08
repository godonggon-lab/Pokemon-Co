from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    value, needed = map(int, data.split())
    value += 1
    while str(value).count("5") < needed:
        value += 1
    return str(value)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n"), edge("4 1\n"), edge("54 2\n"), edge("55 2\n"), edge("500 3\n"), stress("499 2\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
