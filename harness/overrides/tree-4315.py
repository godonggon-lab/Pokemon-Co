from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n1 0 2 2 3\n2 3 0\n3 0 0\n0\n', '3\r\n'),
        edge('1\n1 1 0\n0\n', '0\r\n'),
        stress('5\n1 4 2 2 3\n2 0 1 4\n3 0 1 5\n4 1 0\n5 0 0\n0\n', '4\r\n'),
    ]
