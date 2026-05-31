from __future__ import annotations

import itertools
from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    board = [list(map(int, line.split())) for line in lines[1 : 1 + n]]
    viruses: list[tuple[int, int]] = []
    empty = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                viruses.append((i, j))
            elif board[i][j] == 0:
                empty += 1
    if empty == 0:
        return "0"
    answer = 10**9
    for starts in itertools.combinations(viruses, m):
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        for r, c in starts:
            dist[r][c] = 0
            queue.append((r, c))
        infected = 0
        last = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 1 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    if board[nr][nc] == 0:
                        infected += 1
                        last = dist[nr][nc]
                    queue.append((nr, nc))
        if infected == empty:
            answer = min(answer, last)
    return str(-1 if answer == 10**9 else answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4 1\n2 0 0 0\n1 1 1 0\n0 0 0 0\n0 1 1 2\n",
        "3 2\n2 2 2\n2 2 2\n2 2 2\n",
        "5 2\n2 0 1 0 2\n0 0 1 0 0\n1 1 1 1 1\n0 0 1 0 0\n2 0 1 0 2\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "\n".join([
        "8 3",
        "2 0 0 0 0 0 0 2",
        "0 1 1 1 1 1 1 0",
        "0 1 2 0 0 2 1 0",
        "0 1 0 1 1 0 1 0",
        "0 1 0 0 0 0 1 0",
        "0 1 2 0 0 2 1 0",
        "0 1 1 1 1 1 1 0",
        "2 0 0 0 0 0 0 2",
    ]) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
