from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('7 6\n1 2 3 4 5 6 7\n0 0\n', '0\r\n'),
        edge('10 9\n1 3 4 5 8 9 15 30 31 32\n0 0\n', '4\r\n'),
        edge('1 1\n1\n0 0\n', '0\r\n'),
        edge('5 4\n1 2 3 4 5\n0 0\n', '0\r\n'),
        edge('7 5\n1 2 3 5 6 8 9\n0 0\n', '2\r\n'),
        stress('12 11\n1 2 3 5 6 7 10 11 12 20 21 22\n0 0\n', '3\r\n'),
    ]
