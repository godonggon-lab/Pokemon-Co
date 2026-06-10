from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n = int(data)
    mod = 1_000_000_007
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % mod
    return str(a)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("0\n"), edge("1\n"), edge("2\n"), edge("10\n"), edge("100\n"), stress("1000000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
