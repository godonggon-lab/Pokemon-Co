from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    queries = nums[1:]
    max_n = max(queries)
    dp = [0] * (max_n + 3)
    dp[0] = 1
    for i in range(1, max_n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return "\n".join(str(dp[n]) for n in queries) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n"),
        edge("1\n2\n"),
        edge("1\n3\n"),
        edge("3\n4\n5\n6\n"),
        edge("5\n1\n2\n3\n10\n11\n"),
        stress("11\n" + "\n".join(str(i) for i in range(1, 12)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
