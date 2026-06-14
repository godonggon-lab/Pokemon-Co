from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    start, end = map(int, lines[1].split())
    links = [[] for _ in range(n + 1)]
    for line in lines[2 : 2 + m]:
        a, b = map(int, line.split())
        links[a].append(b)
        links[b].append(a)
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == end:
            break
        for nxt in (cur - 1, cur + 1):
            if 1 <= nxt <= n and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
        for nxt in links[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    return str(dist[end])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "10 1\n1 10\n1 10\n",
        "10 0\n2 9\n",
        "7 2\n1 7\n2 6\n3 7\n",
        "5 0\n3 3\n",
        "6 2\n1 6\n1 4\n4 6\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    teleports = "\n".join(f"{i} {1000 - i + 1}" for i in range(1, 101))
    stdin = f"1000 100\n1 1000\n{teleports}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
