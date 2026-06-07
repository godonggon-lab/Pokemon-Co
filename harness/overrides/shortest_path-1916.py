from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\n1\n1 2 5\n1 2\n', '5\r\n'),
        edge('5\n8\n1 2 2\n1 3 3\n2 3 1\n2 4 5\n3 4 1\n4 5 2\n1 5 20\n3 5 10\n1 5\n', '6\r\n'),
        edge('3\n3\n1 2 10\n1 2 1\n2 3 1\n1 3\n', '2\r\n'),
        stress('20\n19\n1 2 1\n2 3 2\n3 4 3\n4 5 4\n5 6 5\n6 7 6\n7 8 7\n8 9 8\n9 10 9\n10 11 10\n11 12 11\n12 13 12\n13 14 13\n14 15 14\n15 16 15\n16 17 16\n17 18 17\n18 19 18\n19 20 19\n1 20\n', '190\r\n'),
    ]
