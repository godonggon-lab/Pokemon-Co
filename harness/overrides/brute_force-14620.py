from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    from itertools import combinations

    lines = data.splitlines()
    n = int(lines[0])
    board = [list(map(int, line.split())) for line in lines[1:1 + n]]
    candidates = [(i, j) for i in range(1, n - 1) for j in range(1, n - 1)]
    shape = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    best = 10**18
    for selected in combinations(candidates, 3):
        used = set()
        total = 0
        ok = True
        for x, y in selected:
            for dx, dy in shape:
                nx, ny = x + dx, y + dy
                if (nx, ny) in used:
                    ok = False
                    break
                used.add((nx, ny))
                total += board[nx][ny]
            if not ok:
                break
        if ok:
            best = min(best, total)
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("6\n1 1 1 1 1 1\n1 1 1 1 1 1\n1 1 1 1 1 1\n1 1 1 1 1 1\n1 1 1 1 1 1\n1 1 1 1 1 1\n"),
        edge("6\n9 9 9 9 9 9\n9 1 1 1 1 9\n9 1 9 9 1 9\n9 1 9 9 1 9\n9 1 1 1 1 9\n9 9 9 9 9 9\n"),
        edge("7\n1 2 3 4 5 6 7\n7 6 5 4 3 2 1\n1 2 3 4 5 6 7\n7 6 5 4 3 2 1\n1 2 3 4 5 6 7\n7 6 5 4 3 2 1\n1 2 3 4 5 6 7\n"),
        edge("8\n1 1 1 1 1 1 1 1\n1 9 9 9 9 9 9 1\n1 9 1 1 1 1 9 1\n1 9 1 9 9 1 9 1\n1 9 1 9 9 1 9 1\n1 9 1 1 1 1 9 1\n1 9 9 9 9 9 9 1\n1 1 1 1 1 1 1 1\n"),
        edge("10\n1 2 3 4 5 6 7 8 9 10\n2 3 4 5 6 7 8 9 10 1\n3 4 5 6 7 8 9 10 1 2\n4 5 6 7 8 9 10 1 2 3\n5 6 7 8 9 10 1 2 3 4\n6 7 8 9 10 1 2 3 4 5\n7 8 9 10 1 2 3 4 5 6\n8 9 10 1 2 3 4 5 6 7\n9 10 1 2 3 4 5 6 7 8\n10 1 2 3 4 5 6 7 8 9\n"),
        stress("10\n5 5 5 5 5 5 5 5 5 5\n5 1 5 1 5 1 5 1 5 5\n5 5 5 5 5 5 5 5 5 5\n5 1 5 1 5 1 5 1 5 5\n5 5 5 5 5 5 5 5 5 5\n5 1 5 1 5 1 5 1 5 5\n5 5 5 5 5 5 5 5 5 5\n5 1 5 1 5 1 5 1 5 5\n5 5 5 5 5 5 5 5 5 5\n5 5 5 5 5 5 5 5 5 5\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
