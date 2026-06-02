from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    prices = [0] + list(map(int, lines[1].split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - j] + prices[j] for j in range(1, i + 1))
    return str(dp[n])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n5\n"), edge("4\n1 5 6 7\n"), edge("5\n10 9 8 7 6\n"), stress("20\n" + " ".join(str((i * 13) % 100 + 1) for i in range(1, 21)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
