from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    r, c = map(int, lines[0].split())
    k = int(lines[1])
    grid = lines[2 : 2 + r]
    idx = {"J": 0, "O": 1, "I": 2}
    prefix = [[[0, 0, 0] for _ in range(c + 1)] for _ in range(r + 1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            for z in range(3):
                prefix[i][j][z] = prefix[i - 1][j][z] + prefix[i][j - 1][z] - prefix[i - 1][j - 1][z]
            prefix[i][j][idx[grid[i - 1][j - 1]]] += 1
    out = []
    for line in lines[2 + r : 2 + r + k]:
        a, b, x, y = map(int, line.split())
        out.append(" ".join(str(prefix[x][y][z] - prefix[a - 1][y][z] - prefix[x][b - 1][z] + prefix[a - 1][b - 1][z]) for z in range(3)))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 3\n3\nJOI\nIOJ\n1 1 2 3\n1 1 1 1\n2 2 2 3\n",
        "1 1\n1\nJ\n1 1 1 1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = ["".join("JOI"[(i + j) % 3] for j in range(30)) for i in range(30)]
    queries = "\n".join(["1 1 30 30", "5 5 20 25", "10 1 30 10"] * 10)
    stdin = f"30 30\n30\n" + "\n".join(rows) + "\n" + queries + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
