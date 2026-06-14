from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n, a, b, c, d = map(int, stdin.split())
    answer = 10**30
    for x in range(min(c, n // a + 2) + 1):
        remain = max(0, n - a * x)
        y = (remain + c - 1) // c
        answer = min(answer, b * x + d * y)
    for y in range(min(a, n // c + 2) + 1):
        remain = max(0, n - c * y)
        x = (remain + a - 1) // a
        answer = min(answer, b * x + d * y)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "10 3 5 4 6\n",
        "1 10 100 20 150\n",
        "100 6 10 9 14\n",
        "12 3 4 5 100\n",
        "17 4 100 6 7\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("1000000000 99991 123456 88889 111111\n", _solve("1000000000 99991 123456 88889 111111\n")))
    return cases
