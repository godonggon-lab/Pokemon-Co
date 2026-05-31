from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    t = int(lines[0])
    pos = 1
    answers: list[str] = []
    for _ in range(t):
        n, d = map(int, lines[pos].split())
        pos += 1
        arr = [list(map(int, lines[pos + i].split())) for i in range(n)]
        pos += n
        mid = n // 2
        for _step in range((d % 360) // 45):
            old = [row[:] for row in arr]
            for i in range(n):
                arr[i][mid] = old[i][i]
                arr[i][n - 1 - i] = old[i][mid]
                arr[mid][n - 1 - i] = old[i][n - 1 - i]
                arr[i][i] = old[mid][i]
        answers.extend(" ".join(map(str, row)) for row in arr)
    return "\n".join(answers)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n3 45\n1 2 3\n4 5 6\n7 8 9\n",
        "1\n3 -45\n1 2 3\n4 5 6\n7 8 9\n",
        "2\n1 270\n7\n5 90\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    grid = "\n".join(" ".join(str(i * 7 + j + 1) for j in range(7)) for i in range(7))
    hard = f"1\n7 315\n{grid}\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
