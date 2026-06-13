from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 1\n1\n1 1 1\n', '1\r\n'),
        edge('3 2 3\n1 1 1\n1 1 1\n1 1 1\n1 1 1\n2 2 2\n', '1\r\n'),
        edge('1 0 5\n5\n', '0\r\n'),
        edge('1 1 1\n0\n1 1 5\n', '1\r\n'),
        edge('2 2 1\n0 0\n0 0\n1 1 1\n1 1 1\n', '2\r\n'),
        stress('4 4 5\n2 3 2 3\n3 2 3 2\n2 3 2 3\n3 2 3 2\n1 1 1\n1 4 2\n4 1 3\n4 4 4\n', '30\r\n'),
    ]
