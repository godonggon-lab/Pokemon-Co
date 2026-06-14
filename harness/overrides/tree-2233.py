from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n01\n1 2\n', '1 2\r\n'),
        edge('3\n001101\n2 5\n', '0 0\r\n'),
        edge('1\n01\n1 1\n', '1 2\r\n'),
        edge('2\n0011\n1 4\n', '1 4\r\n'),
        edge('2\n0101\n1 3\n', '0 0\r\n'),
        stress('5\n0001101101\n3 8\n', '1 8\r\n'),
    ]
