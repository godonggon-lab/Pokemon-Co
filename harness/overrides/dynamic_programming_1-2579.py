from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    stairs = [0] + nums[1:]
    if n == 1:
        return f"{stairs[1]}\n"
    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n10\n"),
        edge("2\n10\n20\n"),
        edge("3\n10\n20\n15\n"),
        edge("4\n10\n20\n15\n25\n"),
        edge("6\n10\n20\n15\n25\n10\n20\n"),
        stress("10\n" + "\n".join(str((i * 7) % 30 + 1) for i in range(10)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
