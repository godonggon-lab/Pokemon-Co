from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n_text, digit = data.split()
    n = int(n_text)
    return str(sum(str(value).count(digit) for value in range(1, n + 1)))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("10 0\n"),
        edge("9 9\n"),
        edge("100 1\n"),
        edge("999 9\n"),
        edge("1234 2\n"),
        stress("100000 7\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
