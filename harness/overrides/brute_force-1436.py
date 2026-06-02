from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    target = int(data)
    count = 0
    number = 666
    while True:
        if "666" in str(number):
            count += 1
            if count == target:
                return str(number)
        number += 1


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("2\n"),
        edge("6\n"),
        edge("10\n"),
        edge("100\n"),
        stress("500\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
