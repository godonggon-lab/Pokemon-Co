from __future__ import annotations

from itertools import combinations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _connected(group: set[int], graph: list[list[int]]) -> bool:
    if not group:
        return False
    stack = [next(iter(group))]
    seen = {stack[0]}
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if nxt in group and nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return len(seen) == len(group)


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    populations = [0] + list(map(int, lines[1].split()))
    graph = [[] for _ in range(n + 1)]
    for node, line in enumerate(lines[2:2 + n], start=1):
        values = list(map(int, line.split()))
        graph[node] = values[1:]
    districts = set(range(1, n + 1))
    answer = 10**9
    for size in range(1, n // 2 + 1):
        for selected in combinations(range(1, n + 1), size):
            a = set(selected)
            b = districts - a
            if _connected(a, graph) and _connected(b, graph):
                answer = min(answer, abs(sum(populations[i] for i in a) - sum(populations[i] for i in b)))
    return str(answer if answer < 10**9 else -1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n10 20\n1 2\n1 1\n"),
        edge("3\n1 2 3\n1 2\n2 1 3\n1 2\n"),
        edge("4\n5 5 5 5\n1 2\n2 1 3\n2 2 4\n1 3\n"),
        edge("4\n1 10 100 1000\n0\n0\n0\n0\n"),
        edge("5\n10 20 30 40 50\n2 2 3\n2 1 4\n2 1 5\n1 2\n1 3\n"),
        stress("6\n2 3 5 7 11 13\n2 2 3\n2 1 4\n2 1 5\n2 2 6\n1 3\n1 4\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
