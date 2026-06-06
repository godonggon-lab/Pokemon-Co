from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n1 1\n', '1\r\n'),
        edge('1\n5\n1 5\n2 4\n3 3\n4 2\n5 1\n', '5\r\n'),
        edge('1\n5\n1 1\n2 2\n3 3\n4 4\n5 5\n', '1\r\n'),
        edge('2\n3\n1 3\n2 1\n3 2\n4\n4 1\n3 2\n2 3\n1 4\n', '2\r\n4\r\n'),
        stress('1\n20\n1 20\n2 19\n3 18\n4 17\n5 16\n6 15\n7 14\n8 13\n9 12\n10 11\n11 10\n12 9\n13 8\n14 7\n15 6\n16 5\n17 4\n18 3\n19 2\n20 1\n', '20\r\n'),
    ]
