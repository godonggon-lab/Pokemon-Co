from __future__ import annotations
import math
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    x, y, target = map(float, data.split())
    low, high = 0.0, min(x, y)
    for _ in range(100):
        mid = (low + high) / 2
        h1 = math.sqrt(x * x - mid * mid)
        h2 = math.sqrt(y * y - mid * mid)
        current = h1 * h2 / (h1 + h2)
        if current > target:
            low = mid
        else:
            high = mid
    return f"{low:.3f}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("30 40 10\n"), edge("10 10 5\n"), stress("100 120 30\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
