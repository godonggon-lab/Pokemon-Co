from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    x, y, p1, p2 = map(int, data.split())
    seen = {p1 + x * i for i in range(10000)}
    for j in range(10000):
        value = p2 + y * j
        if value in seen:
            return str(value)
    return "-1"

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("2 4 1 3\n"), edge("4 6 1 2\n"), stress("7 11 5 9\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
