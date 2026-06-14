from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3 1\n0 0 0\n1 0 1\n0 1 0\n', '3\r\n'),
        edge('5 5 2\n1 0 1 0 1\n0 1 0 1 0\n1 0 1 0 1\n0 0 0 0 0\n1 1 1 1 1\n', '11\r\n'),
        edge('1 3 1\n0 0 0\n', '0\r\n'),
        edge('1 3 1\n0 1 0\n', '1\r\n'),
        edge('1 3 1\n1 1 1\n', '3\r\n'),
        stress('6 6 3\n0 1 0 1 0 1\n1 0 0 0 1 0\n0 0 1 0 0 1\n1 0 0 1 0 0\n0 1 0 0 1 0\n1 1 1 0 0 0\n', '13\r\n'),
    ]
