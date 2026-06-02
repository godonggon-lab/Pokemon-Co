from __future__ import annotations

from collections import deque
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
    color = [0] * (n + 1)
    for start in range(1, n + 1):
        if color[start]:
            continue
        color[start] = 1
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if color[nxt] == color[node]:
                    return "0"
                if color[nxt] == 0:
                    color[nxt] = -color[node]
                    queue.append(nxt)
    return "1"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 2\n1 2\n2 3\n"),
        edge("3 3\n1 2\n2 3\n1 3\n"),
        stress("6 5\n1 2\n2 3\n3 4\n4 5\n5 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
