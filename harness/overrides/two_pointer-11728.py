from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    a = list(map(int, lines[1].split()))
    b = list(map(int, lines[2].split()))
    return " ".join(map(str, sorted(a + b)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "2 2\n3 5\n2 9\n",
        "1 1\n1\n2\n",
        "3 4\n-3 0 2\n-4 -1 2 8\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    a = " ".join(map(str, range(0, 2000, 2)))
    b = " ".join(map(str, range(1, 2000, 2)))
    stdin = f"1000 1000\n{a}\n{b}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
