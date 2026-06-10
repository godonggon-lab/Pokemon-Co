from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    n, m, k = tokens[0], tokens[1], tokens[2]
    idx = 3
    tabs = []
    max_cost = 0
    for _ in range(n):
        cpu, memory, cost = tokens[idx], tokens[idx + 1], tokens[idx + 2]
        idx += 3
        tabs.append((cpu, memory, cost))
        max_cost += cost
    neg = -10**18
    dp = [[neg] * (max_cost + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for cpu, memory, cost in tabs:
        next_dp = [row[:] for row in dp]
        for cur_cpu in range(m + 1):
            for cur_cost in range(max_cost - cost + 1):
                if dp[cur_cpu][cur_cost] == neg:
                    continue
                next_cpu = min(m, cur_cpu + cpu)
                next_dp[next_cpu][cur_cost + cost] = max(next_dp[next_cpu][cur_cost + cost], dp[cur_cpu][cur_cost] + memory)
        dp = next_dp
    for cost, memory in enumerate(dp[m]):
        if memory >= k:
            return f"{cost}\n"
    return "-1\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("4 8 3\n4 1 1\n4 2 2\n7 1 2\n7 3 3\n"),
        edge("2 10 10\n3 3 1\n4 4 1\n"),
        edge("1 5 5\n5 5 0\n"),
        edge("3 5 5\n5 1 10\n1 5 1\n4 4 2\n"),
        edge("4 10 1\n3 10 1\n3 10 1\n4 0 1\n10 1 5\n"),
        stress("5 10 12\n4 5 1\n6 4 2\n3 9 3\n10 1 4\n2 8 1\n"),
    ])
