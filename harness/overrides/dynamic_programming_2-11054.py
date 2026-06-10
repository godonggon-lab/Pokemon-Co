from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    a = nums[1:]
    inc = [1] * n
    dec = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                inc[i] = max(inc[i], inc[j] + 1)
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if a[j] < a[i]:
                dec[i] = max(dec[i], dec[j] + 1)
    return f"{max(inc[i] + dec[i] - 1 for i in range(n))}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n"),
        edge("10\n1 5 2 1 4 3 4 5 2 1\n"),
        edge("5\n1 2 3 4 5\n"),
        edge("5\n5 4 3 2 1\n"),
        edge("7\n3 3 3 3 3 3 3\n"),
        stress("50\n" + " ".join(str((i*17)%30) for i in range(50)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
