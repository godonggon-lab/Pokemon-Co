from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]
    board = [nums[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    stack = [(0, 0)]
    seen = [[False] * n for _ in range(n)]
    while stack:
        y, x = stack.pop()
        if y >= n or x >= n or seen[y][x]:
            continue
        if board[y][x] == -1:
            return "HaruHaru\n"
        seen[y][x] = True
        jump = board[y][x]
        stack.append((y + jump, x))
        stack.append((y, x + jump))
    return "Hing\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2\n1 1\n1 -1\n",
        "2\n2 1\n1 -1\n",
        "3\n2 2 1\n1 2 1\n1 1 -1\n",
        "3\n1 1 1\n2 2 1\n1 1 -1\n",
        "4\n2 3 1 1\n1 2 1 1\n1 1 1 1\n1 1 1 -1\n",
        "4\n3 3 3 3\n3 3 3 3\n3 3 3 3\n3 3 3 -1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "5\n1 1 1 1 1\n4 4 4 4 1\n1 1 1 4 1\n1 4 1 1 1\n1 1 1 1 -1\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
