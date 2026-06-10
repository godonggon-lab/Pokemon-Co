from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data.strip())
    dp = [0] * (n + 1)
    dp[1] = 1
    for year in range(2, n + 1):
        born = dp[year - 1] * 2
        dead = 0
        for birth in range(1, year):
            age = year - birth
            if (birth <= 3 and age == 4) or (birth >= 4 and age == 3):
                dead += dp[birth] - (dp[birth - 1] * 2 if birth > 1 else 0)
        dp[year] = born - dead
    return f"{dp[n]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("3\n"), edge("4\n"), edge("7\n"), stress("10\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
