from __future__ import annotations

import bisect
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    points = sorted(map(int, lines[1].split()))
    out = []
    for line in lines[2:]:
        a, b = map(int, line.split())
        out.append(str(bisect.bisect_right(points, b) - bisect.bisect_left(points, a)))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5 3\n1 3 10 20 30\n1 10\n5 25\n-10 0\n",
        "1 2\n7\n7 7\n8 9\n",
        "6 4\n-5 -1 0 2 2 9\n-5 2\n2 2\n-10 10\n3 8\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    points = " ".join(str(i * 2 - 1000) for i in range(1000))
    queries = "\n".join(f"{i - 1000} {i + 100}" for i in range(0, 1000, 10))
    stdin = f"1000 100\n{points}\n{queries}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
