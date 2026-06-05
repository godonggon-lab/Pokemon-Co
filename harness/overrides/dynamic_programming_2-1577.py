from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, m = nums[:2]
    k = nums[2]
    idx = 3
    blocked = set()
    for _ in range(k):
        a, b, c, d = nums[idx : idx + 4]
        idx += 4
        blocked.add(tuple(sorted(((a, b), (c, d)))))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if i and tuple(sorted(((i - 1, j), (i, j)))) not in blocked:
                dp[i][j] += dp[i - 1][j]
            if j and tuple(sorted(((i, j - 1), (i, j)))) not in blocked:
                dp[i][j] += dp[i][j - 1]
    return f"{dp[n][m]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 2\n0\n"),
        edge("2 2\n1\n0 0 1 0\n"),
        stress("4 3\n3\n0 0 1 0\n1 1 1 2\n2 2 3 2\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
