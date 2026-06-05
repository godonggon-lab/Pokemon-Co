from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 0\n0\n', '1\r\n'),
        edge('2 2 1\n01\n10\n', '3\r\n'),
        stress('4 5 2\n01000\n11110\n00000\n01111\n', '8\r\n'),
    ]
