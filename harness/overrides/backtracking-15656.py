from __future__ import annotations

from itertools import product
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    values = sorted(map(int, lines[1].split()))
    return "\n".join(" ".join(map(str, p)) for p in product(values, repeat=m))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n42\n"),
        edge("2 2\n2 1\n"),
        edge("3 2\n4 2 9\n"),
        edge("4 3\n10 1 7 3\n"),
        edge("5 1\n5 4 3 2 1\n"),
        stress("7 3\n7 1 6 2 5 3 4\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
