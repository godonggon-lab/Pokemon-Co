from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    woks = list(map(int, lines[1].split()))
    sizes = set(woks)
    for i in range(m):
        for j in range(i + 1, m):
            sizes.add(woks[i] + woks[j])
    inf = 10**9
    dp = [inf] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for size in sizes:
            if i >= size:
                dp[i] = min(dp[i], dp[i - size] + 1)
    return str(dp[n] if dp[n] < inf else -1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5 1\n2\n"),
        edge("10 3\n1 3 4\n"),
        stress("31 4\n3 5 9 11\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
