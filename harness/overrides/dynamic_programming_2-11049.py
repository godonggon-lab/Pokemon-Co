from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    mat = [(nums[i], nums[i + 1]) for i in range(1, 2 * n, 2)]
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            dp[left][right] = 10**18
            for mid in range(left, right):
                cost = dp[left][mid] + dp[mid + 1][right] + mat[left][0] * mat[mid][1] * mat[right][1]
                dp[left][right] = min(dp[left][right], cost)
    return f"{dp[0][n - 1]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n5 7\n"), edge("3\n5 3\n3 2\n2 6\n"), stress("5\n10 20\n20 5\n5 30\n30 2\n2 8\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
