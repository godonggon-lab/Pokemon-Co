from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    board = [[0] * 100 for _ in range(100)]
    for line in lines[1:]:
        x, y = map(int, line.split())
        for r in range(y, y + 10):
            for c in range(x, x + 10):
                board[r][c] = 1
    heights = [0] * 100
    answer = 0
    for r in range(100):
        for c in range(100):
            heights[c] = heights[c] + 1 if board[r][c] else 0
        stack: list[int] = []
        for i in range(101):
            cur = heights[i] if i < 100 else 0
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                answer = max(answer, h * (i - left))
            stack.append(i)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n0 0\n", "2\n0 0\n10 0\n", "3\n0 0\n5 0\n0 5\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    coords = "\n".join(f"{(i * 7) % 90} {(i * 11) % 90}" for i in range(30))
    stdin = f"30\n{coords}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
