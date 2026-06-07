from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n', '0\r\n'),
        edge('1\n2\n', '1\r\n'),
        edge('4\n1 3 5 7\n', '3\r\n'),
        edge('5\n2 4 6 8 10\n', '1\r\n'),
        edge('6\n997 991 1 0 3 4\n', '3\r\n'),
        stress('10\n2 3 5 7 11 13 17 19 23 29\n', '10\r\n'),
    ]
