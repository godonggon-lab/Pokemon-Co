from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    idx = 0
    t = values[idx]
    idx += 1
    out = []
    for _ in range(t):
        n = values[idx]
        idx += 1
        coins = values[idx:idx + n]
        idx += n
        target = values[idx]
        idx += 1
        dp = [0] * (target + 1)
        dp[0] = 1
        for coin in coins:
            for value in range(coin, target + 1):
                dp[value] += dp[value - coin]
        out.append(str(dp[target]))
    return "\n".join(out) + "\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1\n2\n1 2\n5\n"), edge("2\n3\n1 5 10\n100\n2\n2 3\n10\n"), stress("1\n5\n1 2 5 10 20\n200\n")])
