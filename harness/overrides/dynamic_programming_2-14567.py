from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, m = nums[:2]
    graph = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        a, b = nums[idx], nums[idx + 1]
        idx += 2
        graph[a].append(b)
        indeg[b] += 1
    dp = [1] * (n + 1)
    q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
                dp[nxt] = max(dp[nxt], dp[cur] + 1)
    return " ".join(map(str, dp[1:])) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 0\n"),
        edge("3 0\n"),
        edge("3 2\n1 2\n2 3\n"),
        edge("4 3\n1 3\n2 3\n3 4\n"),
        edge("5 4\n1 2\n1 3\n2 4\n3 5\n"),
        stress("6 6\n1 3\n2 3\n3 4\n3 5\n4 6\n5 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
