from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    k = int(lines[1])
    blocked = set()
    for line in lines[2:2 + k]:
        a, b, c, d = map(int, line.split())
        blocked.add(tuple(sorted(((a, b), (c, d)))))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for x in range(n + 1):
        for y in range(m + 1):
            if x < n and tuple(sorted(((x, y), (x + 1, y)))) not in blocked:
                dp[x + 1][y] += dp[x][y]
            if y < m and tuple(sorted(((x, y), (x, y + 1)))) not in blocked:
                dp[x][y + 1] += dp[x][y]
    return str(dp[n][m])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n0\n"), edge("2 2\n1\n0 0 1 0\n"), stress("4 3\n3\n0 0 1 0\n1 1 1 2\n3 2 4 2\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
