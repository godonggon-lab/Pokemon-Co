from __future__ import annotations

from itertools import permutations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n, m = map(int, stdin.split())
    return "\n".join(" ".join(map(str, p)) for p in permutations(range(1, n + 1), m))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n"),
        edge("2 1\n"),
        edge("2 2\n"),
        edge("3 1\n"),
        edge("3 2\n"),
        stress("4 2\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
