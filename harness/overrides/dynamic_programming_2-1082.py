from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _better(a: str, b: str) -> str:
    if len(a) != len(b):
        return a if len(a) > len(b) else b
    return a if a > b else b


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    price = nums[1 : 1 + n]
    m = nums[1 + n]
    dp = [""] * (m + 1)
    if n > 0 and price[0] <= m:
        dp[price[0]] = "0"
    for cost in range(m + 1):
        if not dp[cost]:
            continue
        for digit in range(n):
            if dp[cost] == "0":
                continue
            nc = cost + price[digit]
            if nc <= m:
                dp[nc] = _better(dp[nc], dp[cost] + str(digit))
    for digit in range(1, n):
        if price[digit] <= m:
            dp[price[digit]] = _better(dp[price[digit]], str(digit))
            for cost in range(price[digit], m + 1):
                if not dp[cost]:
                    continue
                for nd in range(n):
                    nc = cost + price[nd]
                    if nc <= m:
                        dp[nc] = _better(dp[nc], dp[cost] + str(nd))
    ans = "0"
    for value in dp:
        if value:
            ans = _better(ans, value)
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n6 7 8\n21\n"),
        edge("2\n1 10\n9\n"),
        stress("5\n5 3 4 6 7\n24\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
