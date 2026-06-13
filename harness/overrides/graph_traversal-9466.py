from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n3\n1 2 3\n', '0\r\n'),
        edge('1\n7\n3 1 3 7 3 4 6\n', '3\r\n'),
        edge('1\n3\n2 3 3\n', '2\r\n'),
        edge('1\n4\n2 1 4 3\n', '0\r\n'),
        edge('1\n4\n2 1 4 4\n', '1\r\n'),
        stress('1\n20\n2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 1\n', '0\r\n'),
    ]
