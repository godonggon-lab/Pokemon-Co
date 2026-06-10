from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, d = map(int, lines[0].split())
    shortcuts = [[] for _ in range(d + 1)]
    for line in lines[1:1 + n]:
        a, b, c = map(int, line.split())
        if b <= d and b - a > c:
            shortcuts[b].append((a, c))
    dp = list(range(d + 1))
    for i in range(1, d + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        for a, c in shortcuts[i]:
            dp[i] = min(dp[i], dp[a] + c)
    return str(dp[d])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("0 10\n"),
        edge("1 10\n0 10 20\n"),
        edge("2 10\n0 5 3\n5 10 3\n"),
        edge("3 10\n0 3 1\n3 7 2\n7 10 1\n"),
        edge("2 5\n0 6 1\n1 5 10\n"),
        stress("5 50\n0 10 5\n10 20 5\n0 30 20\n25 50 10\n40 45 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
