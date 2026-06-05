from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    queries = [int(line) for line in lines[1:1 + t]]
    mod = 1_000_000_009
    max_n = max(queries)
    dp = [0] * (max(4, max_n + 1))
    dp[0] = 1
    for i in range(1, max_n + 1):
        dp[i] = ((dp[i - 1] if i >= 1 else 0) + (dp[i - 2] if i >= 2 else 0) + (dp[i - 3] if i >= 3 else 0)) % mod
    return "\n".join(str(dp[n]) for n in queries)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("3\n1\n2\n3\n"), edge("4\n4\n7\n10\n100\n"), stress("5\n1000\n10000\n100000\n500000\n1000000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
