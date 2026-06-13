from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5\n1 2 3 4 6\n', '3\r\n'),
        edge('6\n0 0 0 0 0 0\n', '5\r\n'),
        edge('1\n0\n', '0\r\n'),
        edge('4\n0 0 0 0\n', '3\r\n'),
        edge('4\n1 1 2 3\n', '1\r\n'),
        stress('10\n-3 -1 0 1 2 3 5 8 13 21\n', '6\r\n'),
    ]
