from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n = int(lines[0])
    dp = []
    for i in range(n):
        row = list(map(int, lines[i + 1].split()))
        if i == 0:
            dp = row
            continue
        ndp = [0] * (i + 1)
        for j in range(i + 1):
            best = 0
            if j < i:
                best = max(best, dp[j])
            if j > 0:
                best = max(best, dp[j - 1])
            ndp[j] = best + row[j]
        dp = ndp
    return f"{max(dp)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n"),
        edge("3\n1\n2 3\n4 5 6\n"),
        stress("20\n" + "\n".join(" ".join(str((r * c + c) % 99 + 1) for c in range(1, r + 2)) for r in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
