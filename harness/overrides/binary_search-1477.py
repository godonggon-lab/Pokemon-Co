from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, add_count, road_length = map(int, lines[0].split())
    rests = sorted([0] + (list(map(int, lines[1].split())) if n else []) + [road_length])
    low, high = 1, road_length
    answer = high
    while low <= high:
        mid = (low + high) // 2
        needed = sum((rests[i + 1] - rests[i] - 1) // mid for i in range(n + 1))
        if needed <= add_count:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("0 1 10\n\n"),
        edge("0 2 10\n\n"),
        edge("1 1 10\n5\n"),
        edge("2 1 20\n5 15\n"),
        edge("3 2 100\n20 50 80\n"),
        stress("5 3 200\n20 60 90 140 170\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
