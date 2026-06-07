from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 1\n1\n', '1\r\n'),
        edge('2 1 2\n1 2\n1\n2\n', '2\r\n1\r\n'),
        edge('3 1 3\n1 2\n1 3\n1\n2\n3\n', '3\r\n1\r\n1\r\n'),
        edge('5 1 3\n1 2\n1 3\n3 4\n3 5\n1\n3\n4\n', '5\r\n3\r\n1\r\n'),
        edge('6 3 4\n1 2\n2 3\n3 4\n3 5\n5 6\n3\n5\n6\n1\n', '6\r\n2\r\n1\r\n1\r\n'),
        stress('7 1 4\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7\n1\n2\n3\n7\n', '7\r\n3\r\n3\r\n1\r\n'),
    ]
