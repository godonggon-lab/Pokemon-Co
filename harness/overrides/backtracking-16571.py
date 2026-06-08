from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    board = [list(map(int, line.split())) for line in data.splitlines()]

    def win(player: int) -> bool:
        lines = list(board)
        lines += [[board[i][j] for i in range(3)] for j in range(3)]
        lines += [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
        return any(all(value == player for value in line) for line in lines)

    turn = 1 if sum(row.count(1) for row in board) == sum(row.count(2) for row in board) else 2

    def game(player: int) -> int:
        if win(3 - player):
            return -1
        best = -2
        moved = False
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    moved = True
                    board[i][j] = player
                    best = max(best, -game(3 - player))
                    board[i][j] = 0
        return 0 if not moved else best

    result = game(turn)
    return "W" if result == 1 else ("L" if result == -1 else "D")


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 2 1\n2 1 2\n0 0 0\n"),
        edge("1 0 0\n0 0 0\n0 0 0\n"),
        edge("1 1 0\n2 2 0\n0 0 0\n"),
        edge("1 2 1\n0 2 0\n0 0 0\n"),
        edge("1 2 0\n0 1 0\n2 0 0\n"),
        stress("1 2 1\n2 1 0\n0 0 2\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
