from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    board = [list(map(int, line.split())) for line in lines[1:1 + n]]
    cells = [[], []]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cells[(i + j) & 1].append((i, j))

    def count_bishops(group: list[tuple[int, int]]) -> int:
        diag1 = [False] * (2 * n)
        diag2 = [False] * (2 * n)
        best = 0

        def dfs(index: int, count: int) -> None:
            nonlocal best
            if index == len(group):
                best = max(best, count)
                return
            if count + len(group) - index <= best:
                return
            x, y = group[index]
            if not diag1[x + y] and not diag2[x - y + n]:
                diag1[x + y] = diag2[x - y + n] = True
                dfs(index + 1, count + 1)
                diag1[x + y] = diag2[x - y + n] = False
            dfs(index + 1, count)

        dfs(0, 0)
        return best

    return str(count_bishops(cells[0]) + count_bishops(cells[1]))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n"),
        edge("3\n1 1 1\n1 1 1\n1 1 1\n"),
        stress("5\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
