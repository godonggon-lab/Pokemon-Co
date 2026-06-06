from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 1\n', '1\r\n'),
        edge('2\n1 2\n2 3\n', '2\r\n'),
        edge('3\n1 4\n2 3\n3 5\n', '2\r\n'),
        edge('5\n0 0\n0 1\n1 1\n1 2\n2 2\n', '5\r\n'),
        edge('6\n1 4\n2 4\n3 4\n4 4\n4 5\n5 6\n', '4\r\n'),
        stress('10\n1 10\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n8 9\n9 10\n10 11\n', '9\r\n'),
    ]
