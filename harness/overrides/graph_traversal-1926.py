from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n0\n', '0\r\n0\r\n'),
        edge('1 1\n1\n', '1\r\n1\r\n'),
        edge('3 3\n1 1 0\n0 1 0\n1 0 1\n', '3\r\n3\r\n'),
        edge('4 5\n1 1 0 0 0\n1 0 0 1 1\n0 0 1 1 1\n1 0 0 0 0\n', '3\r\n5\r\n'),
        edge('2 3\n1 1 1\n1 1 1\n', '1\r\n6\r\n'),
        stress('10 10\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n', '50\r\n1\r\n'),
    ]
