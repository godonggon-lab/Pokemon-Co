from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2\n', '2 1 1\r\n'),
        edge('6 7\n3 6\n4 3\n3 2\n1 3\n1 2\n2 4\n5 2\n', '4 2 3\r\n'),
        stress('20 19\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n8 9\n9 10\n10 11\n11 12\n12 13\n13 14\n14 15\n15 16\n16 17\n17 18\n18 19\n19 20\n', '20 19 1\r\n'),
    ]
