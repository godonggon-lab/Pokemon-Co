from __future__ import annotations

from itertools import combinations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n = int(stdin)
    values = []
    for length in range(1, 11):
        for comb in combinations(range(10), length):
            values.append(int("".join(map(str, sorted(comb, reverse=True)))))
    values.sort()
    return str(values[n] if n < len(values) else -1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("0\n"),
        edge("9\n"),
        edge("10\n"),
        edge("18\n"),
        edge("100\n"),
        stress("1023\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
