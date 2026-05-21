from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n"),
        edge("1 1\n1\n"),
        edge("2 2\n10\n01\n"),
        edge("3 3\n111\n111\n111\n"),
        edge("4 5\n10101\n01010\n10101\n01010\n"),
        stress("6 6\n101010\n010101\n101010\n010101\n101010\n010101\n"),
    ]
