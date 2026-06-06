from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 2\n', '1\r\n'),
        edge('3\n1 3\n2 4\n3 5\n', '2\r\n'),
        edge('3\n1 2\n2 3\n3 4\n', '1\r\n'),
        edge('4\n1 10\n2 3\n3 4\n4 5\n', '2\r\n'),
        edge('5\n5 6\n1 2\n3 4\n2 3\n4 5\n', '1\r\n'),
        stress('20\n1 11\n2 12\n3 13\n4 14\n5 15\n6 16\n7 17\n8 18\n9 19\n10 20\n11 21\n12 22\n13 23\n14 24\n15 25\n16 26\n17 27\n18 28\n19 29\n20 30\n', '10\r\n'),
    ]
