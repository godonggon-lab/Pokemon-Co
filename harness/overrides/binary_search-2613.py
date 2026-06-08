from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, groups_target = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    def ok(limit: int) -> bool:
        count = 1
        total = 0
        for value in nums:
            if value > limit:
                return False
            if total + value > limit:
                count += 1
                total = value
            else:
                total += value
        return count <= groups_target

    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if ok(mid):
            high = mid
        else:
            low = mid + 1
    limit = low
    groups = []
    total = count = 0
    remaining = groups_target
    for index, value in enumerate(nums):
        if total + value > limit or n - index < remaining:
            groups.append(count)
            remaining -= 1
            total = value
            count = 1
        else:
            total += value
            count += 1
    groups.append(count)
    return f"{limit}\n{' '.join(map(str, groups))}"

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n7\n"),
        edge("5 2\n1 2 3 4 5\n"),
        edge("6 3\n5 5 5 5 5 5\n"),
        edge("5 5\n1 2 3 4 5\n"),
        edge("7 2\n10 1 1 1 1 1 10\n"),
        stress("8 4\n1 100 1 100 1 100 1 100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
