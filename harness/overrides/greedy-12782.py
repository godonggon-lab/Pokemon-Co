from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0 1\n', '1\r\n'),
        edge('1\n1010 0101\n', '2\r\n'),
        edge('2\n1111 0000\n0000 1111\n', '4\r\n4\r\n'),
        edge('3\n1100 1001\n101010 010101\n000 000\n', '1\r\n3\r\n0\r\n'),
        stress('1\n0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101 1010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010\n', '50\r\n'),
    ]
