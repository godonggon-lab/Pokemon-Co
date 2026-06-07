from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0\n0\n', '0\r\n'),
        edge('1\n0\n1\n', '1\r\n'),
        edge('2\n00\n11\n', '1\r\n'),
        edge('3\n000\n010\n', '3\r\n'),
        edge('10\n0000000000\n1111111111\n', '4\r\n'),
        stress('30\n010101010101010101010101010101\n101010101010101010101010101010\n', '10\r\n'),
    ]
