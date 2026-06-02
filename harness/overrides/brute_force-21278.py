from __future__ import annotations

from collections import deque
from itertools import combinations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    graph = [[] for _ in range(n + 1)]
    for line in lines[1:1 + m]:
        a, b = map(int, line.split())
        graph[a].append(b)
        graph[b].append(a)
    best = (10**9, n + 1, n + 1)
    for first, second in combinations(range(1, n + 1), 2):
        dist = [10**9] * (n + 1)
        dist[first] = dist[second] = 0
        queue = deque([first, second])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if dist[nxt] == 10**9:
                    dist[nxt] = dist[node] + 1
                    queue.append(nxt)
        total = sum(dist[1:])
        if (total, first, second) < best:
            best = (total, first, second)
    total, first, second = best
    return f"{first} {second} {total * 2}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1\n1 2\n"),
        edge("3 2\n1 2\n2 3\n"),
        edge("4 3\n1 2\n2 3\n3 4\n"),
        edge("5 4\n1 2\n1 3\n1 4\n1 5\n"),
        edge("5 5\n1 2\n2 3\n3 4\n4 5\n1 5\n"),
        stress("6 7\n1 2\n1 3\n2 4\n3 4\n4 5\n5 6\n2 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
