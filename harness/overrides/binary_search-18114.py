from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, target = map(int, lines[0].split())
    weights = sorted(map(int, lines[1].split()))
    if target in weights:
        return "1"
    for i in range(n):
        for j in range(i + 1, n):
            current = weights[i] + weights[j]
            if current == target:
                return "1"
            if current < target:
                index = bisect.bisect_left(weights, target - current, j + 1)
                if index < n and weights[index] == target - current:
                    return "1"
    return "0"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 5\n5\n"), edge("3 10\n1 4 5\n"), stress("5 20\n2 7 9 11 14\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
