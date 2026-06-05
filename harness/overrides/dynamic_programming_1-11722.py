from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    dp = [1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                dp[j] = max(dp[j], dp[i] + 1)
    return str(max(dp))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("5\n5 4 3 2 1\n"),
        edge("5\n1 2 3 4 5\n"),
        edge("6\n10 30 10 20 20 10\n"),
        edge("6\n1 1 1 1 1 1\n"),
        stress("20\n" + " ".join(str(20 - ((i * 7) % 23)) for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
