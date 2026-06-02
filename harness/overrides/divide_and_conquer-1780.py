from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    board = [list(map(int, line.split())) for line in lines[1:1 + n]]
    counts = {-1: 0, 0: 0, 1: 0}

    def solve(r: int, c: int, size: int) -> None:
        first = board[r][c]
        if all(board[i][j] == first for i in range(r, r + size) for j in range(c, c + size)):
            counts[first] += 1
            return
        third = size // 3
        for dr in range(3):
            for dc in range(3):
                solve(r + dr * third, c + dc * third, third)

    solve(0, 0, n)
    return f"{counts[-1]}\n{counts[0]}\n{counts[1]}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n0\n"),
        edge("3\n1 1 1\n1 1 1\n1 1 1\n"),
        edge("3\n-1 0 1\n-1 0 1\n-1 0 1\n"),
        stress("9\n" + "\n".join(" ".join(str((r + c) % 3 - 1) for c in range(9)) for r in range(9)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
