from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    queries = [tuple(map(int, line.split())) for line in lines[1:1 + t]]
    mod = 1_000_000_009
    max_n = max(n for n, _ in queries)
    max_m = max(m for _, m in queries)
    dp = [[0] * (max_m + 1) for _ in range(max_n + 1)]
    dp[0][0] = 1
    for total in range(1, max_n + 1):
        for count in range(1, max_m + 1):
            dp[total][count] = sum(dp[total - x][count - 1] for x in (1, 2, 3) if total >= x) % mod
    return "\n".join(str(dp[n][m]) for n, m in queries)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 1\n"),
        edge("3\n3 2\n4 2\n5 3\n"),
        edge("3\n10 1\n10 5\n10 10\n"),
        edge("4\n2 1\n2 2\n3 1\n3 3\n"),
        edge("3\n6 2\n6 3\n6 6\n"),
        stress("3\n100 50\n200 100\n1000 500\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
