from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    dp = list(range(n + 1))
    for i in range(1, int(n**0.5) + 1):
        sq = i * i
        for v in range(sq, n + 1):
            dp[v] = min(dp[v], dp[v - sq] + 1)
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("4\n"), edge("11\n"), edge("999\n"), stress("5000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
