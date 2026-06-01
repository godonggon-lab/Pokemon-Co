from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n, target = map(int, data.split())
    low, high = 1, target
    answer = target
    while low <= high:
        mid = (low + high) // 2
        count = sum(min(n, mid // i) for i in range(1, n + 1))
        if count >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n1\n"), edge("3\n7\n"), stress("1000\n500000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
