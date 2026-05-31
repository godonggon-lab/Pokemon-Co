from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    m, n = map(int, lines[0].split())
    grid = [list(line) for line in lines[1 : 1 + m]]
    used = [[False] * n for _ in range(m)]
    answer = 0
    for r in range(m - 1):
        for c in range(n):
            if grid[r][c] == grid[r + 1][c] == "X" and not used[r][c] and not used[r + 1][c]:
                if c + 1 < n and grid[r][c + 1] == grid[r + 1][c + 1] == ".":
                    used[r][c] = used[r + 1][c] = True
                    answer += 1
                elif c - 1 >= 0 and grid[r][c - 1] == grid[r + 1][c - 1] == ".":
                    used[r][c] = used[r + 1][c] = True
                    answer += 1
    for r in range(m):
        for c in range(n - 1):
            if grid[r][c] == grid[r][c + 1] == "X" and not used[r][c] and not used[r][c + 1]:
                if r + 1 < m and grid[r + 1][c] == grid[r + 1][c + 1] == ".":
                    used[r][c] = used[r][c + 1] = True
                    answer += 1
                elif r - 1 >= 0 and grid[r - 1][c] == grid[r - 1][c + 1] == ".":
                    used[r][c] = used[r][c + 1] = True
                    answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 2\nXX\n..\n",
        "3 3\nX..\nX..\n...\n",
        "4 4\nXX..\nXX..\n..XX\n..XX\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "6 8\nXX..XX..\nXX..XX..\n........\n..XX..XX\n..XX..XX\n........\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
