from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5 1\n1 2 4 6 7\n', '3\r\n'),
        edge('4 2\n1 3 5 7\n', '0\r\n'),
        edge('1 0\n2\n', '1\r\n'),
        edge('5 0\n2 4 6 8 10\n', '5\r\n'),
        edge('7 2\n2 1 4 3 6 5 8\n', '3\r\n'),
        stress('10 2\n2 4 1 6 8 3 10 12 5 14\n', '6\r\n'),
    ]
