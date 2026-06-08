from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    cols = [[], [], [], []]
    for line in lines[1 : 1 + n]:
        for i, value in enumerate(map(int, line.split())):
            cols[i].append(value)
    left = Counter(x + y for x in cols[0] for y in cols[1])
    answer = sum(left.get(-(x + y), 0) for x in cols[2] for y in cols[3])
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2\n-1 -1 -1 3\n1 1 1 -3\n",
        "1\n0 0 0 0\n",
        "3\n1 2 -3 0\n-1 -2 3 0\n0 0 0 0\n",
        "2\n0 0 0 0\n0 0 0 0\n",
        "3\n1 1 1 -3\n2 2 -2 -2\n3 -1 -1 -1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    rows = "\n".join(f"{i} {-i} {i % 5} {-i % 5}" for i in range(80))
    stdin = f"80\n{rows}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
