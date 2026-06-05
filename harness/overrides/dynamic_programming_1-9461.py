from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    queries = nums[1:]
    max_n = max(queries)
    dp = [0] * max(6, max_n + 1)
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2
    for i in range(6, max_n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    return "\n".join(str(dp[n]) for n in queries) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n"),
        edge("1\n3\n"),
        edge("1\n4\n"),
        edge("3\n5\n6\n7\n"),
        edge("5\n1\n2\n3\n10\n20\n"),
        stress("6\n30\n40\n50\n60\n70\n100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
