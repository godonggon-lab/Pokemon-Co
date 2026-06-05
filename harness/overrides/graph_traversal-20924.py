from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n', '0 0\r\n'),
        edge('2 1\n1 2 5\n', '5 0\r\n'),
        edge('3 1\n1 2 5\n2 3 7\n', '12 0\r\n'),
        edge('3 1\n1 2 5\n1 3 7\n', '0 7\r\n'),
        edge('5 1\n1 2 3\n2 3 4\n2 4 5\n4 5 6\n', '3 11\r\n'),
        stress('7 1\n1 2 1\n2 3 2\n3 4 3\n3 5 4\n5 6 5\n5 7 6\n', '3 10\r\n'),
    ]
