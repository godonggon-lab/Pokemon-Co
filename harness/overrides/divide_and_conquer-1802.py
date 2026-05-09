from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n"),
        edge("2\n0\n1\n"),
        edge("3\n000\n010\n101\n"),
        edge("4\n001\n011\n100\n110\n"),
        edge("5\n0000000\n0001000\n0101010\n1010101\n1110111\n"),
        stress("6\n0\n1\n001\n110\n0001000\n1110111\n"),
    ]
