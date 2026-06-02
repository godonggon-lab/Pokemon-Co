from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    value = min(nums)
    while True:
        if sum(value % num == 0 for num in nums) >= 3:
            return str(value)
        value += 1


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1 1 1 1\n"),
        edge("2 3 4 5 6\n"),
        edge("6 10 15 21 35\n"),
        edge("7 11 13 17 19\n"),
        edge("8 9 10 11 12\n"),
        stress("97 89 83 79 73\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
