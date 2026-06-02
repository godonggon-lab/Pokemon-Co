from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    values = sorted(map(int, lines[1].split()))
    left, right = 0, len(values) - 1
    best = 10**18
    answer = (values[left], values[right])
    while left < right:
        total = values[left] + values[right]
        if abs(total) < best:
            best = abs(total)
            answer = (values[left], values[right])
        if total < 0:
            left += 1
        else:
            right -= 1
    return f"{answer[0]} {answer[1]}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n-1 2\n"),
        edge("3\n1 2 4\n"),
        edge("3\n-8 -3 -1\n"),
        edge("5\n-2 4 -99 -1 98\n"),
        edge("6\n-10 -4 -1 2 7 20\n"),
        stress("10\n-100 -50 -20 -7 -3 2 5 9 40 90\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
