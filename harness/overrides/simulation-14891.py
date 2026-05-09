from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("00000000\n00000000\n00000000\n00000000\n1\n1 1\n"),
        edge("10000000\n01000000\n00100000\n00010000\n1\n1 1\n"),
        edge("10101111\n01111101\n11001110\n00000010\n2\n3 -1\n1 1\n"),
        edge("11111111\n00000000\n11111111\n00000000\n4\n1 1\n2 -1\n3 1\n4 -1\n"),
        edge("10101010\n01010101\n10101010\n01010101\n6\n1 1\n2 1\n3 -1\n4 -1\n1 -1\n4 1\n"),
        stress("10010011\n01010011\n11100011\n01010101\n8\n1 1\n2 1\n3 1\n4 1\n1 -1\n2 -1\n3 -1\n4 -1\n"),
    ]
