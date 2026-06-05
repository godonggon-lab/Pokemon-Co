from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n, m = map(int, lines[0].split())
    a = sorted(map(int, lines[1].split()))
    b = sorted(map(int, lines[2].split()))
    if n > m:
        a, b = b, a
        n, m = m, n
    inf = 10**18
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] + abs(a[i - 1] - b[j - 1]))
    return f"{dp[n][m]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1 1\n10\n20\n"), edge("2 3\n1 10\n2 9 20\n"), stress("4 6\n1 3 20 30\n2 4 5 25 28 40\n")])
