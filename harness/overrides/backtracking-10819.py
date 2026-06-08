from __future__ import annotations

import itertools
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    arr = list(map(int, lines[1].split()))
    best = max(
        sum(abs(p[i] - p[i + 1]) for i in range(len(p) - 1))
        for p in itertools.permutations(arr)
    )
    return str(best)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n1 -1\n"),
        edge("3\n1 2 3\n"),
        edge("4\n-1 -2 -3 -4\n"),
        edge("6\n20 1 15 8 4 10\n"),
        edge("5\n0 0 1 -1 2\n"),
        stress("8\n-100 100 -50 50 -25 25 0 75\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
