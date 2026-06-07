from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n2 1\n1 2\n', '1\r\n'),
        edge('2\n3 3\n1 2\n2 3\n1 3\n5 4\n1 2\n2 3\n3 4\n4 5\n', '2\r\n4\r\n'),
        stress('1\n20 19\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n8 9\n9 10\n10 11\n11 12\n12 13\n13 14\n14 15\n15 16\n16 17\n17 18\n18 19\n19 20\n', '19\r\n'),
    ]
