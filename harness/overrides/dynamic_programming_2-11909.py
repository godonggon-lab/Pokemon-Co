from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    grid = [nums[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    inf = 10**18
    dp = [[inf] * n for _ in range(n)]
    dp[0][0] = 0
    for r in range(n):
        for c in range(n):
            if r > 0:
                dp[r][c] = min(dp[r][c], dp[r - 1][c] + max(0, grid[r][c] - grid[r - 1][c] + 1))
            if c > 0:
                dp[r][c] = min(dp[r][c], dp[r][c - 1] + max(0, grid[r][c] - grid[r][c - 1] + 1))
    return f"{dp[-1][-1]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n"),
        edge("2\n2 1\n1 0\n"),
        edge("2\n1 2\n3 4\n"),
        edge("3\n9 8 7\n6 5 4\n3 2 1\n"),
        edge("3\n1 5 2\n2 4 3\n3 3 9\n"),
        stress("8\n" + "\n".join(" ".join(str((i * 3 + j * 5) % 17 + 1) for j in range(8)) for i in range(8)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
