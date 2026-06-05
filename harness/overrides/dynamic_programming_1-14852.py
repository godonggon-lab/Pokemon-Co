from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)
    mod = 1_000_000_007
    dp = [0] * max(3, n + 1)
    dp[0], dp[1], dp[2] = 1, 2, 7
    extra = dp[0]
    for i in range(3, n + 1):
        dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2] + 2 * extra) % mod
        extra = (extra + dp[i - 2]) % mod
    return str(dp[n] % mod)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("5\n"), stress("20\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
