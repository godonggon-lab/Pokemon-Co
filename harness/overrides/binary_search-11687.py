from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    target = int(data)

    def zeros(value: int) -> int:
        total = 0
        while value:
            value //= 5
            total += value
        return total

    low, high = 0, 5 * target + 5
    while low < high:
        mid = (low + high) // 2
        if zeros(mid) >= target:
            high = mid
        else:
            low = mid + 1
    return str(low if zeros(low) == target else -1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("0\n"), edge("1\n"), edge("5\n"), edge("6\n"), stress("100000000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
