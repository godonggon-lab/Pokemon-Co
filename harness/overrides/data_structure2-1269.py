from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _a, _b = map(int, lines[0].split())
    left = set(map(int, lines[1].split()))
    right = set(map(int, lines[2].split()))
    return str(len(left - right) + len(right - left))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n1\n1\n"),
        edge("1 1\n1\n2\n"),
        edge("3 3\n1 2 3\n2 3 4\n"),
        edge("5 4\n1 2 3 4 5\n6 7 8 9\n"),
        edge("5 5\n-1 0 1 2 3\n0 2 4 6 8\n"),
        stress("10 10\n1 2 3 4 5 6 7 8 9 10\n5 6 7 8 9 10 11 12 13 14\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
