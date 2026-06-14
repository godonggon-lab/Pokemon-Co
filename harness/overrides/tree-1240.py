from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4 2\n1 2 3\n2 3 4\n2 4 5\n1 3\n3 4\n', '7\r\n9\r\n'),
        edge('5 3\n1 2 1\n1 3 2\n3 4 3\n3 5 4\n2 5\n4 5\n1 4\n', '7\r\n7\r\n5\r\n'),
        edge('2 2\n1 2 7\n1 2\n2 2\n', '7\r\n0\r\n'),
        edge('3 2\n1 2 1\n1 3 2\n2 3\n1 1\n', '3\r\n0\r\n'),
        edge('4 2\n1 2 2\n2 3 3\n3 4 4\n1 4\n2 3\n', '9\r\n3\r\n'),
        stress('6 3\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n5 6 2\n1 6\n2 5\n3 4\n', '10\r\n6\r\n2\r\n'),
    ]
