from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n, m = map(int, stdin.split())
    board = [[0] * m for _ in range(n)]
    answer = 0

    def dfs(pos: int) -> None:
        nonlocal answer
        if pos == n * m:
            answer += 1
            return
        r, c = divmod(pos, m)
        dfs(pos + 1)
        if not (r > 0 and c > 0 and board[r - 1][c] and board[r][c - 1] and board[r - 1][c - 1]):
            board[r][c] = 1
            dfs(pos + 1)
            board[r][c] = 0

    dfs(0)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n"),
        edge("1 2\n"),
        edge("2 1\n"),
        edge("2 2\n"),
        edge("2 3\n"),
        stress("3 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
