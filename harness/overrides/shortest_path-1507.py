from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    dist = [list(map(int, line.split())) for line in lines[1 : 1 + n]]
    keep = [[True] * n for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    return "-1"
                if dist[i][j] == dist[i][k] + dist[k][j]:
                    keep[i][j] = False
    answer = sum(dist[i][j] for i in range(n) for j in range(i + 1, n) if keep[i][j])
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3\n0 1 2\n1 0 1\n2 1 0\n",
        "3\n0 2 5\n2 0 2\n5 2 0\n",
        "4\n0 1 3 4\n1 0 2 3\n3 2 0 1\n4 3 1 0\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    n = 12
    rows = []
    for i in range(n):
        rows.append(" ".join(str(abs(i - j)) for j in range(n)))
    hard = f"{n}\n" + "\n".join(rows) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
