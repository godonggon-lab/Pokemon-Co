from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    board = [list(map(int, line.split())) for line in lines[1:1 + n]]
    visited = [[False] * m for _ in range(n)]
    directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
    answer = 0

    def t_shape(x: int, y: int) -> int:
        total = board[x][y]
        wings = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                wings.append(board[nx][ny])
        if len(wings) < 3:
            return 0
        if len(wings) == 4:
            wings.remove(min(wings))
        return total + sum(wings)

    def dfs(x: int, y: int, total: int, depth: int) -> None:
        nonlocal answer
        if depth == 4:
            answer = max(answer, total)
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, total + board[nx][ny], depth + 1)
                visited[nx][ny] = False

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, board[i][j], 1)
            visited[i][j] = False
            answer = max(answer, t_shape(i, j))
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 4\n1 2 3 4\n"),
        edge("4 1\n1\n2\n3\n4\n"),
        edge("2 2\n1 2\n3 4\n"),
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n"),
        edge("4 4\n1 1 1 1\n1 9 9 1\n1 9 9 1\n1 1 1 1\n"),
        stress("5 5\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
