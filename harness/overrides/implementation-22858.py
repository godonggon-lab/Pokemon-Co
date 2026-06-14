from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, k = map(int, lines[0].split())
    s = list(map(int, lines[1].split()))
    d = list(map(int, lines[2].split()))
    for _ in range(k):
        prev = [0] * n
        for i in range(n):
            prev[d[i] - 1] = s[i]
        s = prev
    return " ".join(map(str, s))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5 1\n4 1 3 5 2\n4 3 1 2 5\n",
        "5 2\n4 1 3 5 2\n4 3 1 2 5\n",
        "4 3\n1 2 3 4\n2 3 4 1\n",
        "1 100\n7\n1\n",
        "5 0\n5 4 3 2 1\n2 1 4 5 3\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = " ".join(str(i) for i in range(1, 11))
    d = " ".join(str((i % 10) + 1) for i in range(1, 11))
    hard = f"10 17\n{s}\n{d}\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
