from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n1\n', '1\r\n'),
        edge('5 11\n1 2 3 4 5\n', '3\r\n'),
        edge('5 100\n1 2 3 4 5\n', '0\r\n'),
        edge('10 15\n5 1 3 5 10 7 4 9 2 8\n', '2\r\n'),
        edge('10 10\n1 1 1 1 10 1 1 1 1 1\n', '1\r\n'),
        stress('100 250\n1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1\n', '49\r\n'),
    ]
