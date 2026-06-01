from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, rule_count, target = map(int, lines[0].split())
    rules = [tuple(map(int, line.split())) for line in lines[1:1 + rule_count]]

    def count(box: int) -> int:
        total = 0
        for start, end, step in rules:
            if box >= start:
                total += (min(box, end) - start) // step + 1
        return total

    low, high = 1, n
    while low < high:
        mid = (low + high) // 2
        if count(mid) >= target:
            high = mid
        else:
            low = mid + 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("10 1 3\n1 10 2\n"), edge("10 2 5\n1 5 1\n6 10 1\n"), stress("100 3 20\n1 100 3\n2 80 5\n50 100 7\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
