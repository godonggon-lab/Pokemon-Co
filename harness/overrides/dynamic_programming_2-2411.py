from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    tokens = list(map(int, data.split()))
    idx = 0
    n, m, item_count, obstacle_count = tokens[idx], tokens[idx + 1], tokens[idx + 2], tokens[idx + 3]
    idx += 4
    items = []
    for _ in range(item_count):
        items.append((tokens[idx], tokens[idx + 1]))
        idx += 2
    obstacles = set()
    for _ in range(obstacle_count):
        obstacles.add((tokens[idx], tokens[idx + 1]))
        idx += 2
    points = [(1, 1)] + sorted(items) + [(n, m)]

    def ways(start: tuple[int, int], end: tuple[int, int]) -> int:
        x1, y1 = start
        x2, y2 = end
        if x1 > x2 or y1 > y2:
            return 0
        dp = [[0] * (y2 - y1 + 1) for _ in range(x2 - x1 + 1)]
        dp[0][0] = 1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) in obstacles:
                    dp[x - x1][y - y1] = 0
                    continue
                if x > x1:
                    dp[x - x1][y - y1] += dp[x - x1 - 1][y - y1]
                if y > y1:
                    dp[x - x1][y - y1] += dp[x - x1][y - y1 - 1]
        return dp[-1][-1]

    answer = 1
    for start, end in zip(points, points[1:]):
        answer *= ways(start, end)
    return f"{answer}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("3 3 1 0\n2 2\n"),
        edge("4 4 2 1\n2 2\n3 3\n2 3\n"),
        stress("5 5 3 2\n2 2\n3 4\n5 5\n2 3\n4 4\n"),
    ])
