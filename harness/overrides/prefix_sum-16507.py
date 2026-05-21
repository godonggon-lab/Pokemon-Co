from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    r, c, q = map(int, lines[0].split())
    prefix = [[0] * (c + 1)]
    for i in range(r):
        row = list(map(int, lines[1 + i].split()))
        current = [0]
        acc = 0
        prev = prefix[-1]
        for j, value in enumerate(row, 1):
            acc += value
            current.append(prev[j] + acc)
        prefix.append(current)
    out: list[str] = []
    for line in lines[1 + r : 1 + r + q]:
        r1, c1, r2, c2 = map(int, line.split())
        total = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
        count = (r2 - r1 + 1) * (c2 - c1 + 1)
        out.append(str(total // count))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 3 3\n1 2 3\n4 5 6\n1 1 1 1\n1 1 2 3\n2 2 2 3\n",
        "1 1 1\n7\n1 1 1 1\n",
        "3 3 2\n1 1 1\n2 2 2\n3 3 3\n1 1 3 3\n2 2 3 3\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = [" ".join(str((i + j) % 10) for j in range(20)) for i in range(20)]
    queries = ["1 1 20 20", "5 5 10 10", "1 10 20 20"] * 10
    stdin = "20 20 30\n" + "\n".join(rows) + "\n" + "\n".join(queries) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
