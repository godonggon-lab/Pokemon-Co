from __future__ import annotations

from itertools import permutations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    a, b = data.split()
    limit = int(b)
    answer = -1
    for perm in set(permutations(a)):
        if perm[0] == "0":
            continue
        value = int("".join(perm))
        if value < limit:
            answer = max(answer, value)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("123 321\n"),
        edge("100 99\n"),
        edge("100 101\n"),
        edge("11 12\n"),
        edge("987 100\n"),
        stress("987654 700000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
