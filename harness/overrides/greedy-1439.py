from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('0\n', '0\r\n'),
        edge('1\n', '0\r\n'),
        edge('000000\n', '0\r\n'),
        edge('010101\n', '3\r\n'),
        edge('0001100\n', '1\r\n'),
        stress('0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101\n', '50\r\n'),
    ]
