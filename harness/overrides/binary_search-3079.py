from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, target = map(int, lines[0].split())
    times = list(map(int, lines[1:]))
    low, high = 0, 1_000_000_000 * target
    while low <= high:
        mid = (low + high) // 2
        if sum(mid // time for time in times) >= target:
            high = mid - 1
        else:
            low = mid + 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n7\n"),
        edge("1 3\n7\n"),
        edge("2 6\n7\n10\n"),
        edge("2 1\n7\n10\n"),
        edge("3 10\n3\n8\n10\n"),
        stress("5 100\n1\n3\n7\n11\n13\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
