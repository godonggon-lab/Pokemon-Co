from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    a = nums[1:]
    keep = a[0]
    drop = -10**18
    ans = a[0]
    for x in a[1:]:
        drop = max(keep, drop + x)
        keep = max(x, keep + x)
        ans = max(ans, keep, drop)
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n-5\n"),
        edge("5\n1 -2 3 4 -5\n"),
        edge("5\n-1 -2 -3 -4 -5\n"),
        edge("6\n10 -100 20 30 -100 40\n"),
        edge("5\n1 2 3 4 5\n"),
        stress("100\n" + " ".join(str((i * 7) % 31 - 15) for i in range(100)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
