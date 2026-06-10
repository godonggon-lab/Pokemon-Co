from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    idx = 0
    out = []
    while idx < len(nums):
        n = nums[idx]
        idx += 1
        if n == 0:
            break
        best = cur = nums[idx]
        idx += 1
        for _ in range(n - 1):
            x = nums[idx]
            idx += 1
            cur = max(x, cur + x)
            best = max(best, cur)
        out.append(str(best))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n0\n"),
        edge("3\n-1\n-2\n-3\n0\n"),
        edge("5\n1\n2\n-5\n4\n5\n0\n"),
        edge("6\n-5\n4\n-1\n4\n-10\n8\n0\n"),
        edge("2\n7\n-8\n4\n-1\n2\n3\n-2\n0\n"),
        stress("20\n" + "\n".join(str((i * 7) % 21 - 10) for i in range(20)) + "\n0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
