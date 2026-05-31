from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    values = list(map(int, stdin.split()))
    points = [(values[0], values[1]), (values[2], values[3])]
    teleports = []
    for idx in range(4, 16, 4):
        teleports.append((len(points), len(points) + 1))
        points.extend([(values[idx], values[idx + 1]), (values[idx + 2], values[idx + 3])])
    n = len(points)
    dist = [[abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) for j in range(n)] for i in range(n)]
    for a, b in teleports:
        dist[a][b] = dist[b][a] = min(dist[a][b], 10)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return str(dist[0][1])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("0 0\n20 0\n0 0 10 0\n10 0 20 0\n5 5 6 6\n"),
        edge("1 1\n9 9\n1 2 8 8\n2 1 8 7\n0 0 3 3\n"),
        stress("0 0\n100 100\n0 1 99 100\n1 0 100 99\n40 40 60 60\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
