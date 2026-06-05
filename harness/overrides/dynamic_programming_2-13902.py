from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, m = nums[:2]
    woks = nums[2 : 2 + m]
    sizes = set(woks)
    for i in range(m):
        for j in range(i + 1, m):
            sizes.add(woks[i] + woks[j])
    inf = 10**9
    dp = [inf] * (n + 1)
    dp[0] = 0
    for value in range(1, n + 1):
        for size in sizes:
            if value >= size:
                dp[value] = min(dp[value], dp[value - size] + 1)
    return f"{-1 if dp[n] == inf else dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("10 2\n3 5\n"),
        edge("7 3\n2 4 6\n"),
        stress("15 4\n1 3 7 10\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
