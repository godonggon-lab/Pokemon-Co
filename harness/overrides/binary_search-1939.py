from __future__ import annotations
from collections import deque
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    graph = [[] for _ in range(n + 1)]
    high = 0
    for line in lines[1:1 + m]:
        a, b, weight = map(int, line.split())
        graph[a].append((b, weight))
        graph[b].append((a, weight))
        high = max(high, weight)
    start, end = map(int, lines[1 + m].split())

    def can(limit: int) -> bool:
        seen = [False] * (n + 1)
        seen[start] = True
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node == end:
                return True
            for next_node, weight in graph[node]:
                if not seen[next_node] and weight >= limit:
                    seen[next_node] = True
                    queue.append(next_node)
        return False

    low, answer = 1, 0
    while low <= high:
        mid = (low + high) // 2
        if can(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("2 1\n1 2 7\n1 2\n"), edge("3 3\n1 2 3\n2 3 4\n1 3 2\n1 3\n"), stress("5 6\n1 2 5\n2 5 4\n1 3 10\n3 4 3\n4 5 8\n2 4 6\n1 5\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
