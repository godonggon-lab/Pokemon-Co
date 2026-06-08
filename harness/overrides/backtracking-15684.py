from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m, h = map(int, lines[0].split())
    ladder = [[False] * (n + 1) for _ in range(h + 1)]
    for line in lines[1:1 + m]:
        a, b = map(int, line.split())
        ladder[a][b] = True

    def ok() -> bool:
        for start in range(1, n + 1):
            cur = start
            for row in range(1, h + 1):
                if ladder[row][cur]:
                    cur += 1
                elif cur > 1 and ladder[row][cur - 1]:
                    cur -= 1
            if cur != start:
                return False
        return True

    def dfs(pos: int, count: int, limit: int) -> bool:
        if count == limit:
            return ok()
        for idx in range(pos, h * (n - 1)):
            row = idx // (n - 1) + 1
            col = idx % (n - 1) + 1
            if ladder[row][col]:
                continue
            if col > 1 and ladder[row][col - 1]:
                continue
            if col < n - 1 and ladder[row][col + 1]:
                continue
            ladder[row][col] = True
            if dfs(idx + 1, count + 1, limit):
                return True
            ladder[row][col] = False
        return False

    for limit in range(4):
        if dfs(0, 0, limit):
            return str(limit)
    return "-1"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 0 3\n"),
        edge("3 0 3\n"),
        edge("2 1 3\n1 1\n"),
        edge("3 1 3\n2 1\n"),
        edge("4 2 4\n1 1\n3 3\n"),
        stress("5 3 5\n1 1\n3 2\n2 4\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
