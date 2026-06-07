from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2 5\n', '5\r\n'),
        edge('5 6\n1 2 2\n1 3 5\n2 3 1\n2 4 2\n3 5 5\n4 5 1\n', '5\r\n'),
        stress('20 19\n1 2 2\n2 3 3\n3 4 4\n4 5 5\n5 6 6\n6 7 7\n7 8 1\n8 9 2\n9 10 3\n10 11 4\n11 12 5\n12 13 6\n13 14 7\n14 15 1\n15 16 2\n16 17 3\n17 18 4\n18 19 5\n19 20 6\n', '76\r\n'),
    ]
