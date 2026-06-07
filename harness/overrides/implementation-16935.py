from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 2 1\n1 2\n3 4\n1\n', '3 4\r\n1 2\r\n'),
        edge('2 2 2\n1 2\n3 4\n2 1\n', '4 3\r\n2 1\r\n'),
        edge('2 3 1\n1 2 3\n4 5 6\n3\n', '4 1\r\n5 2\r\n6 3\r\n'),
        edge('3 2 1\n1 2\n3 4\n5 6\n4\n', '2 4 6\r\n1 3 5\r\n'),
        edge('4 4 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n5 6 1 2\n', '16 15 14 13\r\n12 11 10 9\r\n8 7 6 5\r\n4 3 2 1\r\n'),
        stress('4 6 6\n1 2 3 4 5 6\n7 8 9 10 11 12\n13 14 15 16 17 18\n19 20 21 22 23 24\n1 2 3 4 5 6\n', '24 23 22 21 20 19\r\n18 17 16 15 14 13\r\n12 11 10 9 8 7\r\n6 5 4 3 2 1\r\n'),
    ]
