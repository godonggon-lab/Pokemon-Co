from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    if n <= 2:
        return str(n)
    best = current = 2
    for i in range(n - 2):
        a, b, c = nums[i], nums[i + 1], nums[i + 2]
        if (a < b < c) or (a > b > c):
            current = 2
        else:
            current += 1
        best = max(best, current)
    return str(best)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5\n1 3 4 2 5\n"),
        edge("6\n1 2 3 4 5 6\n"),
        stress("8\n1 3 2 4 3 5 4 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
