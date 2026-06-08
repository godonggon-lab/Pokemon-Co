from __future__ import annotations
import itertools
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    data = list(map(int, stdin.split()))
    n, _m = data[0], data[1]
    required = set(data[2:])
    return str(sum(1 for password in itertools.product(range(10), repeat=n) if required.issubset(password)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 0\n\n"),
        edge("2 1\n1\n"),
        edge("3 0\n\n"),
        edge("3 2\n0 9\n"),
        edge("4 1\n5\n"),
        stress("4 2\n1 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
