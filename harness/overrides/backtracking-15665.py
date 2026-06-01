from __future__ import annotations

from itertools import product
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    _, m = map(int, data.splitlines()[0].split())
    nums = sorted(set(map(int, data.splitlines()[1].split())))
    return "\n".join(" ".join(map(str, row)) for row in product(nums, repeat=m))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n7\n"),
        edge("2 2\n1 1\n"),
        edge("3 2\n1 1 2\n"),
        edge("4 2\n9 7 9 1\n"),
        edge("5 3\n2 2 1 1 3\n"),
        stress("7 3\n4 4 3 3 2 2 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
