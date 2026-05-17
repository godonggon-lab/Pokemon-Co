from __future__ import annotations

import heapq
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _dijkstra(graph: list[list[tuple[int, int]]], start: int) -> list[int]:
    inf = 10**18
    dist = [inf] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, cur = heapq.heappop(pq)
        if cur_dist != dist[cur]:
            continue
        for nxt, weight in graph[cur]:
            nd = cur_dist + weight
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    return dist


def _solve(stdin: str) -> str:
    it = iter(map(int, stdin.split()))
    n, m, x = next(it), next(it), next(it)
    graph = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, t = next(it), next(it), next(it)
        graph[a].append((b, t))
        rev[b].append((a, t))
    go_home = _dijkstra(graph, x)
    go_party = _dijkstra(rev, x)
    return str(max(go_home[i] + go_party[i] for i in range(1, n + 1)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 1 1\n1 1 1\n",
        "2 2 1\n1 2 5\n2 1 7\n",
        "3 6 2\n1 2 2\n2 1 3\n1 3 4\n3 1 5\n2 3 1\n3 2 1\n",
        "4 8 2\n1 2 4\n1 3 2\n1 4 7\n2 1 1\n2 3 5\n3 1 2\n3 4 4\n4 2 3\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]

    n = 40
    edges = []
    for i in range(1, n):
        edges.append((i, i + 1, i % 9 + 1))
        edges.append((i + 1, i, i % 7 + 1))
    for i in range(1, n - 2):
        edges.append((i, i + 3, 10))
    stdin = f"{n} {len(edges)} 20\n" + "\n".join(f"{a} {b} {c}" for a, b, c in edges) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
