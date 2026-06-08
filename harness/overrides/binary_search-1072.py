from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    games, wins = map(int, data.split())
    current = wins * 100 // games
    if current >= 99:
        return "-1"
    low, high = 1, 10**9
    while low < high:
        mid = (low + high) // 2
        if (wins + mid) * 100 // (games + mid) > current:
            high = mid
        else:
            low = mid + 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("10 8\n"),
        edge("10 0\n"),
        edge("100 80\n"),
        edge("100 99\n"),
        edge("1 0\n"),
        edge("1000 998\n"),
        stress("1000000000 470000000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
