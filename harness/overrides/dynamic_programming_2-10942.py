from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    a = [0] + nums[1 : 1 + n]
    q_start = 1 + n
    m = nums[q_start]
    queries = nums[q_start + 1 :]
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = True
    for i in range(1, n):
        dp[i][i + 1] = a[i] == a[i + 1]
    for length in range(3, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            dp[left][right] = a[left] == a[right] and dp[left + 1][right - 1]
    out = []
    for i in range(0, 2 * m, 2):
        s, e = queries[i], queries[i + 1]
        out.append("1" if dp[s][e] else "0")
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n7\n1\n1 1\n"), edge("5\n1 2 3 2 1\n3\n1 5\n2 4\n1 3\n"), stress("8\n1 2 2 1 3 4 4 3\n5\n1 4\n5 8\n2 3\n3 6\n4 5\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
