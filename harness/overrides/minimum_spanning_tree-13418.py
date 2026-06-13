from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 0\n0 1 0\n', '0\r\n'),
        edge('3 4\n0 1 0\n1 2 1\n2 3 0\n0 2 1\n1 3 0\n', '8\r\n'),
        edge('2 2\n0 1 0\n1 2 0\n0 2 1\n', '3\r\n'),
        edge('2 2\n0 1 1\n1 2 1\n0 2 1\n', '0\r\n'),
        edge('3 3\n0 1 0\n1 2 0\n2 3 0\n0 3 0\n', '0\r\n'),
        stress('4 5\n0 1 0\n1 2 0\n2 3 1\n3 4 0\n0 2 1\n1 4 1\n', '8\r\n'),
    ]
