from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    grid = [list(map(int, line.split())) for line in lines[1 : 1 + n]]
    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            prefix[i][j] = grid[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
    answer = -10**18
    for size in range(1, n + 1):
        for i in range(size, n + 1):
            for j in range(size, n + 1):
                answer = max(answer, prefix[i][j] - prefix[i - size][j] - prefix[i][j - size] + prefix[i - size][j - size])
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n-5\n", "2\n1 2\n3 4\n", "3\n-1 -2 -3\n4 5 6\n-7 8 9\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = "\n".join(" ".join(str((i * j) % 11 - 5) for j in range(20)) for i in range(20))
    stdin = f"20\n{rows}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
