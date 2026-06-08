from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    edges = [tuple(map(int, line.split())) for line in lines[1:1 + m]]
    used = [False] * (n + 1)
    best = 0

    def dfs(index: int, count: int) -> None:
        nonlocal best
        if index == m:
            best = max(best, count)
            return
        a, b = edges[index]
        if not used[a] and not used[b]:
            used[a] = used[b] = True
            dfs(index + 1, count + 2)
            used[a] = used[b] = False
        dfs(index + 1, count)

    dfs(0, 0)
    return str(best + (1 if best < n else 0))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 0\n"),
        edge("2 1\n1 2\n"),
        edge("4 2\n1 2\n3 4\n"),
        edge("5 4\n1 2\n2 3\n3 4\n4 5\n"),
        edge("6 3\n1 2\n2 3\n4 5\n"),
        stress("10 10\n" + "\n".join(f"{i} {i+1}" for i in range(1,10)) + "\n1 10\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
