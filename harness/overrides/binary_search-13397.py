from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, groups_limit = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    def ok(limit: int) -> bool:
        groups = 1
        low = high = nums[0]
        for value in nums[1:]:
            low = min(low, value)
            high = max(high, value)
            if high - low > limit:
                groups += 1
                low = high = value
        return groups <= groups_limit

    left, right = 0, max(nums) - min(nums)
    while left < right:
        mid = (left + right) // 2
        if ok(mid):
            right = mid
        else:
            left = mid + 1
    return str(left)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n7\n"),
        edge("2 1\n1 10\n"),
        edge("5 2\n1 5 4 6 2\n"),
        edge("5 5\n1 5 4 6 2\n"),
        edge("6 3\n3 3 3 3 3 3\n"),
        stress("8 3\n10 1 3 9 4 8 2 7\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
