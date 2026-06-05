from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    dp = [0, 0, 0]
    for line in lines[1:1 + n]:
        r, g, b = map(int, line.split())
        dp = [r + min(dp[1], dp[2]), g + min(dp[0], dp[2]), b + min(dp[0], dp[1])]
    return str(min(dp))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n26 40 83\n"),
        edge("3\n26 40 83\n49 60 57\n13 89 99\n"),
        edge("3\n1 100 100\n100 1 100\n100 100 1\n"),
        edge("4\n10 20 30\n30 20 10\n10 30 20\n20 10 30\n"),
        stress("20\n" + "\n".join(f"{(i*7)%100+1} {(i*11)%100+1} {(i*13)%100+1}" for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
