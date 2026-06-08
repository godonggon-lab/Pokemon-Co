from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    t = [0] * (n + 1)
    p = [0] * (n + 1)
    for i, line in enumerate(lines[1:1 + n]):
        t[i], p[i] = map(int, line.split())
    dp = [0] * (n + 2)
    for day in range(n - 1, -1, -1):
        dp[day] = dp[day + 1]
        if day + t[day] <= n:
            dp[day] = max(dp[day], p[day] + dp[day + t[day]])
    return str(dp[0])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 10\n"),
        edge("1\n2 10\n"),
        edge("3\n1 10\n1 20\n1 30\n"),
        edge("7\n3 10\n5 20\n1 10\n1 20\n2 15\n4 40\n2 200\n"),
        edge("5\n5 100\n4 50\n3 40\n2 30\n1 20\n"),
        stress("15\n" + "\n".join(f"{i%5+1} {(i*13)%100+1}" for i in range(15)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
