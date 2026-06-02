from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = [int(line) for line in lines[1:1 + n]]

    def solve(left: int, right: int, base: int) -> int:
        if left > right:
            return 0
        maximum = max(nums[left:right + 1])
        index = nums.index(maximum, left, right + 1)
        return maximum - base + solve(left, index - 1, maximum) + solve(index + 1, right, maximum)

    return str(solve(0, n - 1, 0))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n1\n2\n3\n"),
        edge("5\n3\n1\n2\n1\n3\n"),
        stress("6\n1\n2\n3\n3\n2\n6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
