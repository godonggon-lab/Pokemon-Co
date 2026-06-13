from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    dp = [[0] * 2001 for _ in range(11)]
    for j in range(1, 2001):
        dp[1][j] = 1
    for i in range(2, 11):
        acc = 0
        for j in range(1, 2001):
            if j % 2 == 0:
                acc += dp[i - 1][j // 2]
            dp[i][j] = acc
    values = list(map(int, data.split()))
    t = values[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m = values[idx], values[idx + 1]
        idx += 2
        out.append(str(sum(dp[n][1:m + 1])))
    return "\n".join(out) + "\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1\n1 10\n"),
        edge("3\n2 10\n3 20\n4 100\n"),
        edge("1\n1 1\n"),
        edge("2\n2 3\n2 4\n"),
        edge("3\n2 100\n3 100\n4 100\n"),
        stress("3\n10 2000\n5 500\n8 1000\n"),
    ])
