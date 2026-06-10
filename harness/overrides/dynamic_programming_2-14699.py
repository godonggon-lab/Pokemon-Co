from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, m = nums[:2]
    heights = [0] + nums[2 : 2 + n]
    graph = [[] for _ in range(n + 1)]
    idx = 2 + n
    for _ in range(m):
        a, b = nums[idx], nums[idx + 1]
        idx += 2
        if heights[a] < heights[b]:
            graph[a].append(b)
        elif heights[b] < heights[a]:
            graph[b].append(a)
    dp = [0] * (n + 1)

    def dfs(node: int) -> int:
        if dp[node]:
            return dp[node]
        dp[node] = 1
        for nxt in graph[node]:
            dp[node] = max(dp[node], dfs(nxt) + 1)
        return dp[node]

    return "\n".join(str(dfs(i)) for i in range(1, n + 1)) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 0\n5\n"),
        edge("3 2\n1 2 3\n1 2\n2 3\n"),
        edge("4 0\n4 3 2 1\n"),
        edge("4 4\n1 4 2 3\n1 2\n1 3\n3 4\n4 2\n"),
        edge("5 4\n5 4 3 2 1\n1 2\n2 3\n3 4\n4 5\n"),
        stress("5 5\n5 1 4 2 3\n1 3\n2 3\n2 4\n4 5\n5 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
