from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]
    graph = [[] for _ in range(n + 1)]
    for i in range(1, len(nums), 3):
        a, b, w = nums[i], nums[i + 1], nums[i + 2]
        graph[a].append((b, w))
        graph[b].append((a, w))

    def far(start: int) -> tuple[int, int]:
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        while q:
            cur = q.popleft()
            for nxt, weight in graph[cur]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[cur] + weight
                    q.append(nxt)
        node = max(range(1, n + 1), key=lambda x: dist[x])
        return node, dist[node]

    return f"{far(far(1)[0])[1]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n1 2 3\n", "3\n1 2 1\n1 3 2\n", "4\n1 2 3\n2 3 4\n2 4 5\n", "5\n1 2 1\n2 3 2\n3 4 3\n4 5 4\n", "6\n1 2 5\n1 3 4\n2 4 3\n2 5 2\n3 6 10\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
