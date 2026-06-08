from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    eggs = [list(map(int, line.split())) for line in lines[1:1 + n]]
    best = 0

    def dfs(index: int) -> None:
        nonlocal best
        if index == n:
            best = max(best, sum(durability <= 0 for durability, _ in eggs))
            return
        if eggs[index][0] <= 0:
            dfs(index + 1)
            return
        hit = False
        for target in range(n):
            if target == index or eggs[target][0] <= 0:
                continue
            hit = True
            eggs[index][0] -= eggs[target][1]
            eggs[target][0] -= eggs[index][1]
            dfs(index + 1)
            eggs[target][0] += eggs[index][1]
            eggs[index][0] += eggs[target][1]
        if not hit:
            dfs(index + 1)

    dfs(0)
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n8 5\n"),
        edge("2\n1 1\n1 1\n"),
        edge("3\n8 5\n1 100\n3 5\n"),
        edge("3\n10 1\n10 1\n10 1\n"),
        edge("4\n2 8\n9 1\n3 5\n6 2\n"),
        stress("5\n10 3\n5 4\n8 2\n1 10\n7 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
