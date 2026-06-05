from __future__ import annotations
from collections import deque
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n = int(lines[0])
    time = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        time[i] = row[0]
        for prev in row[2:]:
            graph[prev].append(i)
            indegree[i] += 1
    queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
    for i in queue:
        dp[i] = time[i]
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            dp[nxt] = max(dp[nxt], dp[node] + time[nxt])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return f"{max(dp)}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1\n5 0\n"), edge("3\n5 0\n10 1 1\n3 1 1\n"), stress("5\n10 0\n5 1 1\n7 1 1\n4 2 2 3\n3 1 4\n")])
