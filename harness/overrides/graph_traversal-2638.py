from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    it = iter(stdin.split())
    n, m = int(next(it)), int(next(it))
    board = [[int(next(it)) for _ in range(m)] for _ in range(n)]
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    hours = 0

    while any(1 in row for row in board):
        outside = [[False] * m for _ in range(n)]
        q: deque[tuple[int, int]] = deque([(0, 0)])
        outside[0][0] = True
        while q:
            y, x = q.popleft()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < n and 0 <= nx < m and not outside[ny][nx] and board[ny][nx] == 0:
                    outside[ny][nx] = True
                    q.append((ny, nx))

        melt: list[tuple[int, int]] = []
        for y in range(n):
            for x in range(m):
                if board[y][x] == 0:
                    continue
                exposed = 0
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < n and 0 <= nx < m and outside[ny][nx]:
                        exposed += 1
                if exposed >= 2:
                    melt.append((y, x))

        for y, x in melt:
            board[y][x] = 0
        hours += 1

    return str(hours)


def _case(rows: list[list[int]]) -> str:
    return f"{len(rows)} {len(rows[0])}\n" + "\n".join(" ".join(map(str, row)) for row in rows) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        _case([
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]),
        _case([
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ]),
        _case([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]),
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]

    rows = [[0] * 20 for _ in range(20)]
    for y in range(2, 18):
        for x in range(2, 18):
            rows[y][x] = 1
    cases.append(stress(_case(rows), _solve(_case(rows))))
    return cases
