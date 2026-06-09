from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    out = []
    nums = list(map(int, data.split()))
    for i in range(0, len(nums), 2):
        n, m = nums[i], nums[i + 1]
        count = 0
        for value in range(n, m + 1):
            text = str(value)
            if len(text) == len(set(text)):
                count += 1
        out.append(str(count))
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 9\n"),
        edge("1 20\n"),
        edge("87 104\n"),
        edge("100 100\n"),
        edge("990 1020\n"),
        stress("1 5000\n5000 10000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
