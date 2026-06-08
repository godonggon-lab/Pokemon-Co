from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, target = map(int, lines[0].split())
    limits = [tuple(map(int, line.split())) for line in lines[1:]]
    if sum(low for low, _ in limits) > target or sum(high for _, high in limits) < target:
        return "-1"
    left, right = 0, 10**9
    while left < right:
        mid = (left + right) // 2
        high_sum = sum(min(high, mid) for _, high in limits)
        if high_sum >= target and all(low <= mid for low, _ in limits):
            right = mid
        else:
            left = mid + 1
    return str(left)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 5\n1 10\n"),
        edge("1 0\n0 10\n"),
        edge("2 100\n1 10\n1 10\n"),
        edge("3 10\n1 5\n2 6\n3 7\n"),
        edge("2 5\n3 3\n2 2\n"),
        stress("20 100\n" + "\n".join(f"{i%3} {i%3+10}" for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
