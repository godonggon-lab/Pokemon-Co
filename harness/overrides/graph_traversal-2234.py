from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n0\n', '1\r\n1\r\n1\r\n'),
        edge('4 3\n11 6 11 6\n7 9 6 13\n7 15 9 6\n', '4\r\n6\r\n9\r\n'),
        stress('5 4\n3 2 6 3 6\n1 0 4 9 4\n9 8 12 3 6\n13 12 13 9 12\n', '5\r\n9\r\n17\r\n'),
    ]
