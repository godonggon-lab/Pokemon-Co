from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n0\n1 1 1\n1 1 1\n', '0\r\n'),
        edge('1 5\n0 0 0 0 0\n1 1 1\n1 5 1\n', '2\r\n'),
        edge('5 1\n0\n0\n0\n0\n0\n1 1 3\n5 1 3\n', '2\r\n'),
        edge('3 3\n0 0 0\n0 1 0\n0 0 0\n1 1 1\n3 3 3\n', '3\r\n'),
        edge('4 5\n0 0 0 0 0\n1 1 0 1 0\n0 0 0 1 0\n0 1 0 0 0\n1 1 1\n4 5 1\n', '5\r\n'),
        stress('5 5\n0 0 0 0 0\n0 1 1 1 0\n0 0 0 1 0\n0 1 0 0 0\n0 0 0 1 0\n1 1 1\n5 5 2\n', '6\r\n'),
    ]
