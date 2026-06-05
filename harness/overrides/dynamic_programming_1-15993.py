from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    queries = [int(line) for line in lines[1:1 + t]]
    mod = 1_000_000_009
    max_n = max(queries)
    dp = [[0, 0] for _ in range(max_n + 1)]
    for x in (1, 2, 3):
        if x <= max_n:
            dp[x][1] = 1
    for total in range(1, max_n + 1):
        for x in (1, 2, 3):
            if total > x:
                dp[total][0] = (dp[total][0] + dp[total - x][1]) % mod
                dp[total][1] = (dp[total][1] + dp[total - x][0]) % mod
    return "\n".join(f"{dp[n][1]} {dp[n][0]}" for n in queries)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("3\n1\n2\n3\n"), edge("3\n4\n7\n10\n"), stress("4\n100\n1000\n10000\n100000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
