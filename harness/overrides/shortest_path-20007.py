from __future__ import annotations

import heapq
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m, x, y = map(int, lines[0].split())
    graph = [[] for _ in range(n)]
    for line in lines[1 : 1 + m]:
        a, b, c = map(int, line.split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    inf = 10**18
    dist = [inf] * n
    dist[y] = 0
    heap = [(0, y)]
    while heap:
        cost, cur = heapq.heappop(heap)
        if cost != dist[cur]:
            continue
        for nxt, weight in graph[cur]:
            nc = cost + weight
            if nc < dist[nxt]:
                dist[nxt] = nc
                heapq.heappush(heap, (nc, nxt))
    if any(value == inf or value * 2 > x for value in dist):
        return "-1"
    days = 1
    today = 0
    for value in sorted(dist):
        trip = value * 2
        if today + trip > x:
            days += 1
            today = 0
        today += trip
    return str(days)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4 3 10 0\n0 1 1\n1 2 2\n2 3 2\n",
        "3 1 4 0\n0 1 3\n",
        "5 5 8 2\n0 2 1\n1 2 2\n2 3 1\n3 4 2\n0 4 5\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    n = 25
    edges = [f"{i} {i + 1} 1" for i in range(n - 1)]
    edges += [f"{i} {i + 2} 3" for i in range(n - 2)]
    hard = f"{n} {len(edges)} 20 0\n" + "\n".join(edges) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
