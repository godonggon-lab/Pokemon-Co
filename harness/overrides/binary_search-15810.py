from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, target = map(int, lines[0].split())
    times = list(map(int, lines[1].split()))
    low, high = 0, min(times) * target
    while low < high:
        mid = (low + high) // 2
        if sum(mid // time for time in times) >= target:
            high = mid
        else:
            low = mid + 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n5\n"), edge("3 10\n1 2 3\n"), stress("20 100000\n" + " ".join(str(i%7+1) for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
