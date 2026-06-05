from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    dp = [0] * max(3, n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("3\n"), edge("10\n"), edge("30\n"), stress("90\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
