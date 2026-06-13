from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    t = int(lines[0])
    idx = 1
    answers = []
    for _ in range(t):
        n, m = map(int, lines[idx].split())
        idx += 1
        row = [0] * n
        col = [0] * n
        for i in range(n):
            values = list(map(int, lines[idx].split()))
            idx += 1
            row[i] = sum(values)
            for j, value in enumerate(values):
                col[j] += value
        for _ in range(m):
            r1, c1, r2, c2, v = map(int, lines[idx].split())
            idx += 1
            for i in range(r1 - 1, r2):
                row[i] += (c2 - c1 + 1) * v
            for j in range(c1 - 1, c2):
                col[j] += (r2 - r1 + 1) * v
        answers.append(" ".join(map(str, row)))
        answers.append(" ".join(map(str, col)))
    return "\n".join(answers)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n2 1\n1 2\n3 4\n1 1 2 2 1\n",
        "1\n3 2\n1 1 1\n2 2 2\n3 3 3\n1 1 1 3 5\n2 2 3 3 -1\n",
        "1\n1 1\n5\n1 1 1 1 -3\n",
        "1\n2 2\n0 0\n0 0\n1 1 1 2 4\n2 1 2 2 7\n",
        "2\n1 0\n9\n2 1\n1 2\n3 4\n1 2 2 2 -2\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    n = 8
    grid = [" ".join(str(i * n + j + 1) for j in range(n)) for i in range(n)]
    queries = [
        "1 1 8 8 3",
        "2 2 7 7 -2",
        "1 4 8 4 5",
        "4 1 4 8 7",
        "3 3 6 6 -4",
    ]
    hard = f"1\n{n} {len(queries)}\n" + "\n".join(grid + queries) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
