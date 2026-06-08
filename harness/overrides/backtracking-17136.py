from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    board = [list(map(int, line.split())) for line in data.splitlines()]
    left = [0, 5, 5, 5, 5, 5]
    best = 26

    def can_place(x: int, y: int, size: int) -> bool:
        if x + size > 10 or y + size > 10:
            return False
        return all(board[i][j] == 1 for i in range(x, x + size) for j in range(y, y + size))

    def fill(x: int, y: int, size: int, value: int) -> None:
        for i in range(x, x + size):
            for j in range(y, y + size):
                board[i][j] = value

    def dfs(count: int) -> None:
        nonlocal best
        if count >= best:
            return
        position = None
        for i in range(10):
            for j in range(10):
                if board[i][j] == 1:
                    position = (i, j)
                    break
            if position:
                break
        if position is None:
            best = min(best, count)
            return
        x, y = position
        for size in range(5, 0, -1):
            if left[size] > 0 and can_place(x, y, size):
                left[size] -= 1
                fill(x, y, size, 0)
                dfs(count + 1)
                fill(x, y, size, 1)
                left[size] += 1

    dfs(0)
    return str(best if best < 26 else -1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge(("0 0 0 0 0 0 0 0 0 0\n"*10)),
        edge(("1 0 0 0 0 0 0 0 0 0\n")+("0 0 0 0 0 0 0 0 0 0\n"*9)),
        edge(("1 1 0 0 0 0 0 0 0 0\n"*2)+("0 0 0 0 0 0 0 0 0 0\n"*8)),
        edge(("1 1 1 1 1 0 0 0 0 0\n"*5)+("0 0 0 0 0 0 0 0 0 0\n"*5)),
        edge(("1 1 1 0 0 0 0 0 0 0\n"*3)+("0 0 0 0 0 0 0 0 0 0\n"*7)),
        stress("1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
