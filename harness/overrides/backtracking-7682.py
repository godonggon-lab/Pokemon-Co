from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    def win(board: str, marker: str) -> bool:
        return any(all(board[index] == marker for index in line) for line in lines)

    out = []
    for board in data.split():
        if board == "end":
            break
        x_count = board.count("X")
        o_count = board.count("O")
        x_win = win(board, "X")
        o_win = win(board, "O")
        ok = False
        if x_count == o_count + 1 and x_win and not o_win:
            ok = True
        if x_count == o_count and o_win and not x_win:
            ok = True
        if x_count == 5 and o_count == 4 and not x_win and not o_win:
            ok = True
        out.append("valid" if ok else "invalid")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("XXXOO.XXX\nend\n"),
        edge("XOXOXOXOX\nend\n"),
        edge(".........\nend\n"),
        edge("XXXOOO...\nend\n"),
        edge("XXOOOXXOX\nend\n"),
        stress(".........\nXXXOOO...\nXXOOOXXOX\nend\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
