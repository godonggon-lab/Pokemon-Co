from __future__ import annotations

import heapq
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    visible = list(map(int, lines[1].split()))
    graph = [[] for _ in range(n)]
    for line in lines[2 : 2 + m]:
        a, b, t = map(int, line.split())
        graph[a].append((b, t))
        graph[b].append((a, t))
    inf = 10**30
    dist = [inf] * n
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        cost, cur = heapq.heappop(heap)
        if cost != dist[cur]:
            continue
        for nxt, weight in graph[cur]:
            if nxt != n - 1 and visible[nxt]:
                continue
            nc = cost + weight
            if nc < dist[nxt]:
                dist[nxt] = nc
                heapq.heappush(heap, (nc, nxt))
    return str(-1 if dist[n - 1] == inf else dist[n - 1])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4 4\n0 0 0 0\n0 1 1\n1 3 2\n0 2 5\n2 3 1\n",
        "4 3\n0 1 0 0\n0 1 1\n1 3 1\n0 2 10\n",
        "3 1\n0 1 1\n0 2 7\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    edges = "\n".join(f"{i} {i + 1} 1" for i in range(199))
    stdin = "200 199\n" + " ".join(["0"] * 200) + "\n" + edges + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
