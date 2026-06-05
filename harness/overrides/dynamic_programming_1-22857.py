from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, k = nums[:2]
    a = nums[2:]
    left = odd = even = ans = 0
    for value in a:
        if value % 2:
            odd += 1
        else:
            even += 1
        while odd > k:
            if a[left] % 2:
                odd -= 1
            else:
                even -= 1
            left += 1
        ans = max(ans, even)
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5 1\n1 2 4 6 7\n"),
        edge("4 2\n1 3 5 7\n"),
        stress("10 3\n1 2 4 5 6 8 10 11 12 14\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
