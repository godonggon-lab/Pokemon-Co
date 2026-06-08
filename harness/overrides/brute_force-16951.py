from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    answer = 10**9
    for first in range(1, 101):
        for diff in range(-99, 100):
            changes = 0
            ok = True
            for i, value in enumerate(nums):
                target = first + diff * i
                if target < 1 or abs(value - target) > 1:
                    ok = False
                    break
                if value != target:
                    changes += 1
            if ok:
                answer = min(answer, changes)
    return str(answer if answer < 10**9 else -1)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("2\n1 100\n"),
        edge("3\n1 2 3\n"),
        edge("4\n1 1 1 1\n"),
        edge("5\n10 8 6 4 2\n"),
        stress("5\n1 3 5 7 8\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
