from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n = int(data)
    mod = 1_000_000_000
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for _ in range(2, n + 1):
        nxt = [0] * 10
        for digit in range(10):
            if digit > 0:
                nxt[digit] += dp[digit - 1]
            if digit < 9:
                nxt[digit] += dp[digit + 1]
        dp = [value % mod for value in nxt]
    return str(sum(dp) % mod)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("10\n"), stress("100\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
