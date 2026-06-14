from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 4 1\n1 2 3 4\n2 3 4 5\n1 0 1\n', '24\r\n'),
        edge('3 4 2\n1 1 2 3\n4 1 1 2\n3 4 4 4\n1 1 1\n2 0 2\n', '13\r\n'),
        edge('1 4 1\n1 2 3 4\n1 0 4\n', '10\r\n'),
        edge('1 4 1\n1 1 1 1\n1 0 1\n', '0\r\n'),
        edge('2 4 1\n1 2 1 2\n2 1 2 1\n2 1 1\n', '0\r\n'),
        stress('4 5 3\n1 2 3 4 5\n5 4 3 2 1\n1 1 1 1 1\n2 2 3 3 4\n1 0 1\n2 1 2\n3 0 3\n', '19\r\n'),
    ]
