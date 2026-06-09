from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, k = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))
    current = sum(nums[:k])
    answer = current
    for i in range(k, n):
        current += nums[i] - nums[i - k]
        answer = max(answer, current)
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n-5\n"),
        edge("4 1\n1 -2 3 -4\n"),
        edge("10 2\n3 -2 -4 -9 0 3 7 13 8 -3\n"),
        edge("5 5\n1 2 3 4 5\n"),
        edge("6 3\n-1 -1 -1 -1 -1 -1\n"),
        stress("100 10\n" + " ".join(str((i * 7) % 31 - 15) for i in range(100)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
