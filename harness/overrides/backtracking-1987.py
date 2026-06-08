from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    rows, cols = map(int, lines[0].split())
    board = lines[1:1 + rows]
    best = 0

    def dfs(x: int, y: int, mask: int, depth: int) -> None:
        nonlocal best
        best = max(best, depth)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                bit = 1 << (ord(board[nx][ny]) - 65)
                if not mask & bit:
                    dfs(nx, ny, mask | bit, depth + 1)

    dfs(0, 0, 1 << (ord(board[0][0]) - 65), 1)
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\nA\n"),
        edge("1 5\nABCDE\n"),
        edge("2 2\nAB\nCD\n"),
        edge("2 4\nCAAB\nADCB\n"),
        edge("3 3\nAAA\nBBB\nCCC\n"),
        stress("3 5\nABCDE\nFGHIJ\nKLMNO\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
