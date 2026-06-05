from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    s = data.strip()
    mod = 1_000_000
    if not s or s[0] == "0":
        return "0\n"
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        two = int(s[i - 2 : i])
        if 10 <= two <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= mod
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("0\n"),
        edge("10\n"),
        edge("25114\n"),
        edge("100\n"),
        stress("11111111111111111111\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
