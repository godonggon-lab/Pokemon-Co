from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n, length, width, height = map(float, data.split())
    low, high = 0.0, min(length, width, height)
    for _ in range(100):
        mid = (low + high) / 2
        if int(length // mid) * int(width // mid) * int(height // mid) >= n:
            low = mid
        else:
            high = mid
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 10 20 30\n"),
        edge("2 10 10 10\n"),
        edge("8 10 10 10\n"),
        edge("27 9 9 9\n"),
        edge("100 10 20 30\n"),
        stress("1000000 100 200 300\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
