from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 1 2\n', '1\r\n'),
        edge('3\n1 1 3\n2 2 4\n3 3 5\n', '2\r\n'),
        edge('3\n1 1 2\n2 2 3\n3 3 4\n', '1\r\n'),
        edge('4\n1 1 10\n2 2 3\n3 3 4\n4 4 5\n', '2\r\n'),
        stress('20\n1 0 10\n2 1 11\n3 2 12\n4 3 13\n5 4 14\n6 0 10\n7 1 11\n8 2 12\n9 3 13\n10 4 14\n11 0 10\n12 1 11\n13 2 12\n14 3 13\n15 4 14\n16 0 10\n17 1 11\n18 2 12\n19 3 13\n20 4 14\n', '20\r\n'),
    ]
