from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, m, k = nums[:3]
    oranges = nums[3:]
    inf = 10**30
    dp = [inf] * n
    for idx in range(n):
        max_size = min_size = oranges[idx]
        for count in range(1, m + 1):
            left = idx - count + 1
            if left < 0:
                break
            max_size = max(max_size, oranges[left])
            min_size = min(min_size, oranges[left])
            prev = dp[left - 1] if left > 0 else 0
            dp[idx] = min(dp[idx], prev + k + count * (max_size - min_size))
    return f"{dp[-1]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1 10\n5\n"),
        edge("2 1 10\n5\n7\n"),
        edge("2 2 10\n5\n7\n"),
        edge("3 2 10\n1\n10\n2\n"),
        edge("5 3 5\n1\n2\n10\n11\n12\n"),
        stress("8 3 7\n1\n3\n6\n10\n15\n21\n28\n36\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
