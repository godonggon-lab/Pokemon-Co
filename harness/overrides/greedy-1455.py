from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n0\n', '0\r\n'),
        edge('1 1\n1\n', '1\r\n'),
        edge('2 2\n10\n01\n', '3\r\n'),
        edge('3 3\n111\n111\n111\n', '1\r\n'),
        edge('4 5\n10101\n01010\n10101\n01010\n', '7\r\n'),
        stress('6 6\n101010\n010101\n101010\n010101\n101010\n010101\n', '11\r\n'),
    ]
