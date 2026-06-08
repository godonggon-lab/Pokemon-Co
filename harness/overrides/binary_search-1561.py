from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    target, ride_count = map(int, lines[0].split())
    rides = list(map(int, lines[1].split()))
    if target <= ride_count:
        return str(target)
    low, high = 0, min(rides) * target
    while low < high:
        mid = (low + high) // 2
        served = ride_count + sum(mid // ride for ride in rides)
        if served >= target:
            high = mid
        else:
            low = mid + 1
    time = low
    served = ride_count + sum((time - 1) // ride for ride in rides)
    for index, ride in enumerate(rides, 1):
        if time % ride == 0:
            served += 1
            if served == target:
                return str(index)
    return ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 3\n2 3 5\n"),
        edge("3 3\n2 3 5\n"),
        edge("4 1\n5\n"),
        edge("6 2\n2 3\n"),
        edge("10 3\n2 2 2\n"),
        stress("100 5\n7 11 13 17 19\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
