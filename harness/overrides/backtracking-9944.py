from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = data.splitlines()
    index = 0
    case_no = 1
    out = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while index < len(tokens):
        n, m = map(int, tokens[index].split())
        index += 1
        board = [list(tokens[index + row]) for row in range(n)]
        index += n
        empty = sum(row.count(".") for row in board)
        best = 10**9

        def dfs(x: int, y: int, left: int, count: int) -> None:
            nonlocal best
            if left == 0:
                best = min(best, count)
                return
            if count >= best:
                return
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                moved = []
                while 0 <= nx < n and 0 <= ny < m and board[nx][ny] == ".":
                    board[nx][ny] = "*"
                    moved.append((nx, ny))
                    nx += dx
                    ny += dy
                if moved:
                    dfs(moved[-1][0], moved[-1][1], left - len(moved), count + 1)
                    for px, py in moved:
                        board[px][py] = "."

        if empty == 1:
            best = 0
        else:
            for i in range(n):
                for j in range(m):
                    if board[i][j] == ".":
                        board[i][j] = "*"
                        dfs(i, j, empty - 1, 0)
                        board[i][j] = "."
        out.append(f"Case {case_no}: {best if best < 10**9 else -1}")
        case_no += 1
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n.\n"),
        edge("2 2\n..\n..\n"),
        edge("2 3\n...\n...\n"),
        edge("3 3\n...\n.*.\n...\n"),
        edge("3 4\n....\n.**.\n....\n"),
        stress("4 4\n....\n.*..\n..*.\n....\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
