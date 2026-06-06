from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 1\n1\n', '1\r\n'),
        edge('5 1 2\n1 3 5 7 9\n', '5\r\n'),
        edge('5 2 3\n1 2 5 8 11\n', '4\r\n'),
        edge('6 10 10\n10 20 10 30 40 50\n', '5\r\n'),
        edge('5 5 1\n1 2 3 4 5\n', '1\r\n'),
        stress('50 3 4\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1 2 3 4 5 6 7 8 9 10\n', '5\r\n'),
    ]
