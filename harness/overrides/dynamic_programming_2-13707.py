from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n, k = map(int, data.split())
    mod = 1_000_000_000
    dp = [0] * (n + 1)
    dp[0] = 1
    for _ in range(k):
        nd = [0] * (n + 1)
        acc = 0
        for i in range(n + 1):
            acc = (acc + dp[i]) % mod
            nd[i] = acc
        dp = nd
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("20 2\n"),
        edge("5 3\n"),
        edge("1 1\n"),
        edge("1 5\n"),
        edge("10 1\n"),
        stress("100 50\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
