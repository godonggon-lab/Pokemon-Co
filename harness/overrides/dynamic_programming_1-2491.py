from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    a = nums[1:]
    inc = dec = ans = 1
    for i in range(1, n):
        inc = inc + 1 if a[i - 1] <= a[i] else 1
        dec = dec + 1 if a[i - 1] >= a[i] else 1
        ans = max(ans, inc, dec)
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n7\n"), edge("5\n1 2 3 4 5\n"), edge("5\n5 4 3 2 1\n"), edge("5\n3 3 3 3 3\n"), edge("8\n1 2 2 3 2 2 1 0\n"), stress("50\n" + " ".join(str((i // 5) % 4) for i in range(50)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
