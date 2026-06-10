from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    target = values[0]
    k = values[1]
    idx = 2
    dp = [0] * (target + 1)
    dp[0] = 1
    for _ in range(k):
        coin, count = values[idx], values[idx + 1]
        idx += 2
        next_dp = dp[:]
        for amount in range(target + 1):
            if dp[amount]:
                for used in range(1, count + 1):
                    nxt = amount + coin * used
                    if nxt <= target:
                        next_dp[nxt] += dp[amount]
        dp = next_dp
    return f"{dp[target]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("5\n1\n5 1\n"), edge("10\n2\n1 10\n5 2\n"), edge("3\n1\n2 1\n"), edge("6\n2\n1 3\n3 1\n"), edge("10\n3\n2 5\n5 1\n10 1\n"), stress("20\n3\n1 5\n5 3\n10 2\n")])
