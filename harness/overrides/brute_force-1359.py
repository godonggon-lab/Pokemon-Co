from __future__ import annotations
from math import comb
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n, m, k = map(int, data.split())
    total = comb(n, m)
    good = sum(comb(m, i) * comb(n - m, m - i) for i in range(k, m + 1) if 0 <= m - i <= n - m)
    return str(good / total)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("10 3 2\n"),
        edge("8 2 1\n"),
        edge("5 1 1\n"),
        edge("6 3 3\n"),
        edge("20 10 0\n"),
        stress("20 5 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
