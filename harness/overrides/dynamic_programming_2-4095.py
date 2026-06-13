from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    idx = 0
    out = []
    while True:
        n, m = tokens[idx], tokens[idx + 1]
        idx += 2
        if n == 0 and m == 0:
            break
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        best = 0
        for i in range(1, n + 1):
            row = tokens[idx:idx + m]
            idx += m
            for j, value in enumerate(row, 1):
                if value:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    best = max(best, dp[i][j])
        out.append(str(best))
    return "\n".join(out) + "\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1 1\n1\n0 0\n"),
        edge("3 3\n1 1 1\n1 1 1\n1 1 1\n0 0\n"),
        edge("2 3\n0 0 0\n0 0 0\n0 0\n"),
        edge("3 4\n1 1 0 1\n1 1 1 1\n0 1 1 1\n0 0\n"),
        edge("1 4\n1 1 1 1\n2 2\n1 0\n0 1\n0 0\n"),
        stress("5 5\n" + "\n".join(" ".join(str((r+c)%2) for c in range(5)) for r in range(5)) + "\n0 0\n"),
    ])
