from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, points = map(int, lines[0].split())
    levels = list(map(int, lines[1:]))
    low, high = min(levels), min(levels) + points + 1
    while low + 1 < high:
        mid = (low + high) // 2
        need = sum(max(0, mid - level) for level in levels)
        if need <= points:
            low = mid
        else:
            high = mid
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 10\n5\n"),
        edge("2 0\n7\n9\n"),
        edge("3 5\n1\n2\n3\n"),
        edge("4 6\n10\n10\n10\n10\n"),
        edge("5 15\n1\n1\n1\n20\n20\n"),
        stress("5 20\n10\n1\n7\n4\n15\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
