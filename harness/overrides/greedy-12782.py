from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0 1\n"),
        edge("1\n1010 0101\n"),
        edge("2\n1111 0000\n0000 1111\n"),
        edge("3\n1100 1001\n101010 010101\n000 000\n"),
        stress("1\n" + "01" * 50 + " " + "10" * 50 + "\n"),
    ]
