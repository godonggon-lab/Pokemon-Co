from __future__ import annotations

import heapq
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    graph = [[] for _ in range(n + 1)]
    for line in lines[1 : 1 + m]:
        a, b, c = map(int, line.split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    s, t = map(int, lines[1 + m].split())
    dist = [10**18] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        cost, node = heapq.heappop(pq)
        if cost != dist[node]:
            continue
        for nxt, weight in graph[node]:
            nc = cost + weight
            if nc < dist[nxt]:
                dist[nxt] = nc
                heapq.heappush(pq, (nc, nxt))
    return str(dist[t])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4 4\n1 2 3\n2 3 4\n3 4 5\n1 4 20\n1 4\n",
        "2 1\n1 2 7\n2 1\n",
        "5 6\n1 2 1\n2 5 1\n1 3 5\n3 4 1\n4 5 1\n2 3 1\n1 5\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    lines = ["30 57"]
    for i in range(1, 30):
        lines.append(f"{i} {i + 1} 1")
    for i in range(1, 29):
        lines.append(f"{i} {i + 2} 3")
    lines.append("1 30")
    hard = "\n".join(lines) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
