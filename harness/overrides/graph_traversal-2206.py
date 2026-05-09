from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n"),
        edge("2 2\n00\n00\n"),
        edge("2 2\n01\n10\n"),
        edge("3 3\n010\n010\n000\n"),
        edge("3 3\n011\n111\n110\n"),
        stress("5 6\n010000\n010111\n000001\n111101\n000000\n"),
    ]
