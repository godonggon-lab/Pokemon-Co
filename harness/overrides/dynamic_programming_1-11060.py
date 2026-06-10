from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    inf = 10**9
    dp = [inf] * n
    dp[0] = 0
    for i in range(n):
        if dp[i] == inf:
            continue
        for jump in range(1, nums[i] + 1):
            if i + jump < n:
                dp[i + jump] = min(dp[i + jump], dp[i] + 1)
    return str(dp[-1] if dp[-1] != inf else -1)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n0\n"),
        edge("2\n1 0\n"),
        edge("5\n1 1 1 1 0\n"),
        edge("5\n0 1 1 1 1\n"),
        edge("6\n5 0 0 0 0 0\n"),
        stress("100\n" + " ".join(str(i%5) for i in range(100)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
