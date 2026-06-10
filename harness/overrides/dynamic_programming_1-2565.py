from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    wires = sorted((nums[i], nums[i + 1]) for i in range(1, 2 * n, 2))
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if wires[j][1] < wires[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return f"{n - max(dp)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 1\n"),
        edge("4\n1 8\n3 9\n2 2\n4 1\n"),
        edge("5\n1 1\n2 2\n3 3\n4 4\n5 5\n"),
        edge("5\n1 5\n2 4\n3 3\n4 2\n5 1\n"),
        edge("6\n10 20\n2 3\n7 9\n4 8\n6 1\n9 10\n"),
        stress("6\n1 3\n2 2\n3 6\n4 4\n5 5\n6 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
