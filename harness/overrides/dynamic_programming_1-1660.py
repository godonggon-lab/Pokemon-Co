from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    tetra = []
    total = 0
    for i in range(1, 200):
        total += i * (i + 1) // 2
        if total > n:
            break
        tetra.append(total)
    dp = [10**9] * (n + 1)
    dp[0] = 0
    for x in tetra:
        for v in range(x, n + 1):
            dp[v] = min(dp[v], dp[v - x] + 1)
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("4\n"), edge("10\n"), edge("15\n"), edge("100\n"), stress("300\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
