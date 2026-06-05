from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n, m = map(int, lines[0].split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    best = 0
    for i in range(1, n + 1):
        for j, ch in enumerate(lines[i].strip(), 1):
            if ch == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                best = max(best, dp[i][j])
    return f"{best * best}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1 1\n0\n"),
        edge("1 1\n1\n"),
        edge("4 4\n1111\n1111\n1111\n1111\n"),
        edge("4 5\n10100\n10111\n11111\n10010\n"),
        stress("20 20\n" + "\n".join(("10" * 10) if i % 2 else ("01" * 10) for i in range(20)) + "\n"),
    ])
