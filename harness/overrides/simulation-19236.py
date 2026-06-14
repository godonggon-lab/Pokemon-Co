from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 2 1 3 1 4 1\n5 1 6 1 7 1 8 1\n9 1 10 1 11 1 12 1\n13 1 14 1 15 1 16 1\n', '1\r\n'),
        edge('7 6 2 3 15 6 9 8\n3 1 1 8 14 7 10 1\n6 1 13 6 4 3 11 4\n16 1 8 7 5 2 12 2\n', '33\r\n'),
        edge('1 2 2 1 3 1 4 1\n5 1 6 1 7 1 8 1\n9 1 10 1 11 1 12 1\n13 1 14 1 15 1 16 1\n', '1\r\n'),
        edge('16 1 15 1 14 1 13 1\n12 1 11 1 10 1 9 1\n8 1 7 1 6 1 5 1\n4 1 3 1 2 1 1 1\n', '16\r\n'),
        edge('1 5 2 5 3 5 4 5\n5 5 6 5 7 5 8 5\n9 5 10 5 11 5 12 5\n13 5 14 5 15 5 16 5\n', '46\r\n'),
        stress('16 7 1 4 4 3 12 8\n14 7 7 6 3 4 10 2\n5 2 15 2 8 3 6 4\n11 8 2 4 13 5 9 4\n', '43\r\n'),
    ]
