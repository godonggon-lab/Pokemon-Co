from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 0\n', '1\r\n'),
        edge('4 2\n4 2\n3 1\n', '3 1 4 2\r\n'),
        edge('5 4\n1 2\n1 3\n3 4\n2 5\n', '1 2 3 4 5\r\n'),
        stress('20 19\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n8 9\n9 10\n10 11\n11 12\n12 13\n13 14\n14 15\n15 16\n16 17\n17 18\n18 19\n19 20\n', '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20\r\n'),
    ]
