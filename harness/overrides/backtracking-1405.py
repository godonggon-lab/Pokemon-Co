from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n, east, west, south, north = map(int, stdin.split())
    probs = [east / 100, west / 100, south / 100, north / 100]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = {(0, 0)}
    answer = 0.0

    def dfs(r: int, c: int, depth: int, prob: float) -> None:
        nonlocal answer
        if depth == n:
            answer += prob
            return
        for (dr, dc), p in zip(dirs, probs):
            if p == 0:
                continue
            nxt = (r + dr, c + dc)
            if nxt in visited:
                continue
            visited.add(nxt)
            dfs(nxt[0], nxt[1], depth + 1, prob * p)
            visited.remove(nxt)

    dfs(0, 0, 0, 1.0)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 100 0 0 0\n"),
        edge("1 25 25 25 25\n"),
        edge("2 50 50 0 0\n"),
        edge("3 25 25 25 25\n"),
        edge("5 100 0 0 0\n"),
        stress("10 25 25 25 25\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
