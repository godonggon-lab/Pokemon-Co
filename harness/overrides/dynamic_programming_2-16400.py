from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    mod = 123456789
    prime = [True] * (n + 1)
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    dp = [0] * (n + 1)
    dp[0] = 1
    for p in range(2, n + 1):
        if not prime[p]:
            continue
        for total in range(p, n + 1):
            dp[total] = (dp[total] + dp[total - p]) % mod
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("2\n"), edge("10\n"), stress("100\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
