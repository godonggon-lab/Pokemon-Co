from __future__ import annotations
from itertools import product
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)
    values = [1, 5, 10, 50]
    seen = set()
    for counts in product(range(n + 1), repeat=4):
        if sum(counts) == n:
            seen.add(sum(count * value for count, value in zip(counts, values)))
    return str(len(seen))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("3\n"), edge("4\n"), edge("5\n"), stress("8\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
