from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, group_count = map(int, lines[0].split())
    scores = list(map(int, lines[1].split()))

    def ok(score: int) -> bool:
        count = current = 0
        for value in scores:
            current += value
            if current >= score:
                count += 1
                current = 0
        return count >= group_count

    low, high = 0, sum(scores)
    while low < high:
        mid = (low + high + 1) // 2
        if ok(mid):
            low = mid
        else:
            high = mid - 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n7\n"), edge("5 2\n1 2 3 4 5\n"), stress("8 3\n10 1 3 9 4 8 2 7\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
