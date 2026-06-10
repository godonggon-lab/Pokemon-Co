from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    idx = 0
    n, m, k = tokens[idx], tokens[idx + 1], tokens[idx + 2]
    idx += 3
    edges = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b, c = tokens[idx], tokens[idx + 1], tokens[idx + 2]
        idx += 3
        if a < b:
            edges[a].append((b, c))
    neg = -10**15
    dp = [[neg] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 0
    for cnt in range(1, m):
        for city in range(1, n + 1):
            if dp[cnt][city] == neg:
                continue
            for nxt, score in edges[city]:
                dp[cnt + 1][nxt] = max(dp[cnt + 1][nxt], dp[cnt][city] + score)
    return f"{max(dp[cnt][n] for cnt in range(1, m + 1))}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("2 2 1\n1 2 5\n"), edge("4 3 5\n1 2 5\n2 4 7\n1 3 10\n3 4 1\n4 1 100\n"), edge("3 2 2\n1 2 5\n2 3 5\n"), edge("3 3 3\n1 2 1\n2 3 100\n1 3 50\n"), edge("4 4 5\n1 2 10\n2 4 10\n1 3 5\n3 4 30\n3 2 100\n"), stress("5 4 7\n1 2 5\n2 3 6\n3 5 7\n1 4 20\n4 5 1\n2 5 8\n5 2 100\n")])
