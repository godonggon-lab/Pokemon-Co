from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n0\n', '0\r\n'),
        edge('3 3\n011\n111\n110\n', '3\r\n'),
        edge('2 2\n00\n00\n', '0\r\n'),
        edge('2 2\n01\n10\n', '1\r\n'),
        edge('4 3\n0110\n0010\n0000\n', '0\r\n'),
        stress('5 4\n01010\n11110\n00010\n01110\n', '2\r\n'),
    ]
