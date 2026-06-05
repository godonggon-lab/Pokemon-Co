from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    queries = [int(line) for line in lines[1:1 + t]]
    mod = 1_000_000_009
    max_n = max(queries)
    dp = [0] * (max_n + 1)
    if max_n >= 0:
        dp[0] = 1
    if max_n >= 1:
        dp[1] = 1
    if max_n >= 2:
        dp[2] = 2
    for n in range(3, max_n + 1):
        dp[n] = (dp[n - 2] + (dp[n - 4] if n >= 4 else 0) + (dp[n - 6] if n >= 6 else 0)) % mod
    return "\n".join(str(dp[n]) for n in queries)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("3\n1\n2\n3\n"), stress("5\n4\n5\n10\n20\n100\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
