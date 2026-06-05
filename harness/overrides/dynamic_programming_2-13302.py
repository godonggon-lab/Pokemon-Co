from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, m = nums[:2]
    closed = set(nums[2 : 2 + m]) if m else set()
    inf = 10**9
    dp = [[inf] * 45 for _ in range(n + 6)]
    dp[0][0] = 0
    for day in range(n):
        for coupon in range(45):
            if dp[day][coupon] == inf:
                continue
            if day + 1 in closed:
                dp[day + 1][coupon] = min(dp[day + 1][coupon], dp[day][coupon])
            else:
                dp[day + 1][coupon] = min(dp[day + 1][coupon], dp[day][coupon] + 10000)
                dp[day + 3][coupon + 1] = min(dp[day + 3][coupon + 1], dp[day][coupon] + 25000)
                dp[day + 5][coupon + 2] = min(dp[day + 5][coupon + 2], dp[day][coupon] + 37000)
                if coupon >= 3:
                    dp[day + 1][coupon - 3] = min(dp[day + 1][coupon - 3], dp[day][coupon])
    return f"{min(dp[n])}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 0\n"), edge("5 2\n2 4\n"), stress("10 3\n2 5 9\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
