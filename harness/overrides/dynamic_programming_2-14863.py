from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, k = nums[:2]
    neg = -10**18
    dp = [neg] * (k + 1)
    dp[0] = 0
    idx = 2
    for _ in range(n):
        walk_t, walk_v, bike_t, bike_v = nums[idx : idx + 4]
        idx += 4
        ndp = [neg] * (k + 1)
        for time, value in enumerate(dp):
            if value == neg:
                continue
            if time + walk_t <= k:
                ndp[time + walk_t] = max(ndp[time + walk_t], value + walk_v)
            if time + bike_t <= k:
                ndp[time + bike_t] = max(ndp[time + bike_t], value + bike_v)
        dp = ndp
    return f"{max(dp)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 10\n5 10 8 20\n"),
        edge("3 10\n5 10 3 8\n4 7 2 4\n4 9 3 5\n"),
        stress("4 15\n5 10 3 6\n4 7 8 20\n6 12 4 8\n3 5 5 9\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
