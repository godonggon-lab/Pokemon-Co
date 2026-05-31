from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    cost = [list(map(int, line.split())) for line in lines[1 : 1 + n]]
    best = 10**18
    visited = [False] * n

    def dfs(cur: int, depth: int, total: int) -> None:
        nonlocal best
        if total >= best:
            return
        if depth == n:
            if cost[cur][0]:
                best = min(best, total + cost[cur][0])
            return
        for nxt in range(n):
            if not visited[nxt] and cost[cur][nxt]:
                visited[nxt] = True
                dfs(nxt, depth + 1, total + cost[cur][nxt])
                visited[nxt] = False

    visited[0] = True
    dfs(0, 1, 0)
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("4\n0 10 15 20\n5 0 9 10\n6 13 0 12\n8 8 9 0\n"),
        edge("3\n0 1 0\n1 0 2\n3 4 0\n"),
        stress("5\n0 7 3 0 2\n4 0 6 5 0\n8 1 0 9 7\n6 4 2 0 3\n5 8 1 6 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
