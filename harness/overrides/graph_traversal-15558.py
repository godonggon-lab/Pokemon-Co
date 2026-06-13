from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4 2\n1111\n1111\n', '1\r\n'),
        edge('5 3\n11011\n00111\n', '1\r\n'),
        edge('2 1\n11\n11\n', '1\r\n'),
        edge('3 1\n100\n000\n', '0\r\n'),
        edge('6 3\n111111\n111111\n', '1\r\n'),
        stress('8 3\n11101111\n10111101\n', '1\r\n'),
    ]
