from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n5 10\n', '5\r\n'),
        edge('3\n1 1\n2 10\n3 1\n', '2\r\n'),
        edge('2\n1 5\n10 5\n', '1\r\n'),
        edge('3\n-10 1\n0 1\n10 1\n', '0\r\n'),
        edge('4\n1 1\n2 1\n3 1\n4 10\n', '4\r\n'),
        stress('5\n10 5\n1 3\n7 20\n20 1\n15 6\n', '7\r\n'),
    ]
