from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n', '0\r\n'),
        edge('3\n111\n000\n111\n', '1\r\n'),
        edge('2\n11\n11\n', '0\r\n'),
        edge('2\n10\n01\n', '1\r\n'),
        edge('3\n100\n000\n001\n', '3\r\n'),
        stress('5\n10101\n10101\n11101\n00001\n11111\n', '1\r\n'),
    ]
