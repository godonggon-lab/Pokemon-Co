from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n1\n0 1 1\n', '1\r\n'),
        edge('3 3\n1 0 2\n0 0 0\n3 0 0\n2 3 2\n', '3\r\n'),
        edge('2 2\n1 0\n0 0\n0 2 2\n', '0\r\n'),
        edge('2 2\n1 2\n0 0\n1 1 2\n', '2\r\n'),
        edge('3 3\n1 0 0\n0 0 0\n0 0 2\n1 3 3\n', '2\r\n'),
        stress('4 4\n1 0 0 0\n0 0 2 0\n0 0 0 0\n3 0 0 4\n3 4 4\n', '4\r\n'),
    ]
