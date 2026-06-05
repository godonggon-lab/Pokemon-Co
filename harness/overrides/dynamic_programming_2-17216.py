from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    idx = 0
    n, m = tokens[idx], tokens[idx + 1]
    idx += 2
    value = [0] + tokens[idx:idx + n]
    idx += n
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = tokens[idx], tokens[idx + 1]
        idx += 2
        graph[b].append(a)
    dp: List[int | None] = [None] * (n + 1)

    def dfs(x: int) -> int:
        if dp[x] is not None:
            return dp[x]
        dp[x] = value[x] + max((dfs(prev) for prev in graph[x]), default=0)
        return dp[x]

    return f"{max(dfs(i) for i in range(1, n + 1))}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("3 2\n1 2 3\n1 2\n2 3\n"), edge("4 3\n5 1 10 2\n1 3\n2 3\n3 4\n"), stress("5 5\n1 4 2 8 3\n1 2\n1 3\n2 4\n3 4\n4 5\n")])
