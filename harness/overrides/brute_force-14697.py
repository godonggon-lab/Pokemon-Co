from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    a, b, c, n = map(int, stdin.split())
    for x in range(n // a + 1):
        for y in range(n // b + 1):
            rest = n - a * x - b * y
            if rest >= 0 and rest % c == 0:
                return "1"
    return "0"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 2 3 1\n",
        "5 9 12 113\n",
        "6 9 20 14\n",
        "7 11 13 1\n",
        "7 11 13 300\n",
        "49 50 51 98\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("17 31 50 299\n", _solve("17 31 50 299\n")))
    return cases
