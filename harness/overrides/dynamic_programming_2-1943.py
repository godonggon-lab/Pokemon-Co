from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    idx = 0
    out = []
    for _ in range(3):
        n = tokens[idx]
        idx += 1
        coins = []
        for _ in range(n):
            value, count = tokens[idx], tokens[idx + 1]
            idx += 2
            coins.append((value, count))
        total = sum(value * count for value, count in coins)
        if total % 2:
            out.append("0")
            continue
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for value, count in coins:
            next_dp = dp[:]
            for cur in range(target + 1):
                if not dp[cur]:
                    continue
                for used in range(1, count + 1):
                    nxt = cur + value * used
                    if nxt > target:
                        break
                    next_dp[nxt] = True
            dp = next_dp
        out.append("1" if dp[target] else "0")
    return "\n".join(out) + "\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("2\n500 1\n100 5\n1\n10 3\n1\n7 1\n"),
        edge("3\n1 1\n2 1\n3 1\n2\n1 5\n2 1\n1\n5 1\n"),
        stress("4\n1 10\n5 3\n10 2\n25 1\n3\n2 5\n4 2\n8 1\n2\n3 3\n9 1\n"),
    ])
