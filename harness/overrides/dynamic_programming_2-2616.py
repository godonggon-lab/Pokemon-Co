from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n = values[0]
    arr = [0] + values[1:1 + n]
    m = values[1 + n]
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i]
    dp = [[0] * (n + 1) for _ in range(4)]
    for train in range(1, 4):
        for i in range(train * m, n + 1):
            block = prefix[i] - prefix[i - m]
            dp[train][i] = max(dp[train][i - 1], dp[train - 1][i - m] + block)
    return f"{dp[3][n]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("3\n1 2 3\n1\n"), edge("6\n1 2 3 4 5 6\n2\n"), edge("6\n10 10 1 1 10 10\n2\n"), edge("9\n1 1 1 100 100 1 1 1 1\n2\n"), edge("12\n1 2 3 4 5 6 7 8 9 10 11 12\n3\n"), stress("9\n5 1 3 8 2 7 4 6 9\n2\n")])
