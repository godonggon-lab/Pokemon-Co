from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n, m = values[0], values[1]
    bad = set(values[2:2 + m])
    inf = 10**9
    limit = int((2 * n) ** 0.5) + 3
    dp = [[inf] * (limit + 1) for _ in range(n + 1)]
    dp[1][0] = 0
    for pos in range(1, n + 1):
        if pos in bad:
            continue
        for jump in range(limit + 1):
            if dp[pos][jump] == inf:
                continue
            for next_jump in (jump - 1, jump, jump + 1):
                next_pos = pos + next_jump
                if next_jump > 0 and next_jump <= limit and next_pos <= n and next_pos not in bad:
                    dp[next_pos][next_jump] = min(dp[next_pos][next_jump], dp[pos][jump] + 1)
    answer = min(dp[n])
    return f"{answer if answer < inf else -1}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("2 0\n"), edge("5 1\n3\n"), edge("3 1\n2\n"), edge("4 0\n"), edge("6 2\n2\n5\n"), stress("10 2\n4\n7\n")])
