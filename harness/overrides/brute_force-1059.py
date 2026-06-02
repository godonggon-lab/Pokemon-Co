from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    nums = sorted(map(int, lines[1].split()))
    target = int(lines[2])
    if target in nums:
        return "0"
    low, high = 0, 1001
    for value in nums:
        if value < target:
            low = value
        elif value > target:
            high = value
            break
    return str((target - low) * (high - target) - 1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n1 7 14\n7\n"),
        edge("3\n1 7 14\n2\n"),
        edge("3\n10 20 30\n5\n"),
        edge("4\n5 10 15 20\n14\n"),
        stress("5\n100 200 300 400 500\n250\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
