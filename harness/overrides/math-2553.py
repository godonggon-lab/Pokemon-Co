from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n = int(stdin.strip())
    value = 1
    for i in range(2, n + 1):
        value *= i
        while value % 10 == 0:
            value //= 10
        value %= 1_000_000
    return str(value % 10)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n", "5\n", "10\n", "20\n", "100\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("1000\n", _solve("1000\n")))
    return cases
