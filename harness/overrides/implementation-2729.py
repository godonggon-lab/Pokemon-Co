from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0 0\n"),
        edge("1\n1 1\n"),
        edge("2\n10 1\n101 11\n"),
        edge("3\n1111 1\n1010 1010\n100000 1\n"),
        edge("4\n0 1\n1 0\n111 111\n1001 1011\n"),
        stress("5\n101010 010101\n111111 1\n1000000 1000000\n1010101010 11110000\n1 1111111111\n"),
    ]
