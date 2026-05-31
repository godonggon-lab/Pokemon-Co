from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, k = map(int, lines[0].split())
    courses = list(map(int, lines[1].split()))
    for idx, length in enumerate(courses, 1):
        if k < length:
            return str(idx)
        k -= length
    for idx in range(n, 0, -1):
        length = courses[idx - 1]
        if k < length:
            return str(idx)
        k -= length
    return "1"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3 0\n2 3 4\n",
        "3 5\n2 3 4\n",
        "3 10\n2 3 4\n",
        "5 27\n1 2 3 4 5\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "10 73\n" + " ".join(str(i) for i in range(1, 11)) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
