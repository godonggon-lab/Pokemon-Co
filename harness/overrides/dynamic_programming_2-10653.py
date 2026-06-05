from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, k = nums[:2]
    pts = [(nums[i], nums[i + 1]) for i in range(2, 2 + 2 * n, 2)]

    def dist(a: int, b: int) -> int:
        return abs(pts[a][0] - pts[b][0]) + abs(pts[a][1] - pts[b][1])

    inf = 10**12
    dp = [[inf] * (k + 1) for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, n):
        for skipped in range(k + 1):
            for prev in range(i):
                add_skip = i - prev - 1
                if skipped >= add_skip:
                    dp[i][skipped] = min(dp[i][skipped], dp[prev][skipped - add_skip] + dist(prev, i))
    return f"{min(dp[-1])}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 0\n0 0\n1 1\n2 2\n"),
        edge("4 1\n0 0\n10 0\n10 10\n20 10\n"),
        stress("6 2\n0 0\n1 2\n4 2\n4 8\n9 8\n9 9\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
