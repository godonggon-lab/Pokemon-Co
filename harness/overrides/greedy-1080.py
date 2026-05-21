from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n1\n"),
        edge("3 3\n000\n000\n000\n111\n111\n111\n"),
        edge("3 3\n000\n000\n000\n100\n000\n000\n"),
        edge("4 4\n0000\n0000\n0000\n0000\n1110\n1110\n1110\n0000\n"),
        edge("5 5\n10101\n01010\n10101\n01010\n10101\n10101\n01010\n10101\n01010\n10101\n"),
        stress("6 7\n0000000\n0000000\n0000000\n0000000\n0000000\n0000000\n1110000\n1110000\n1110000\n0000000\n0000000\n0000000\n"),
    ]
