from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4 4\n1 2 1\n2 3 2\n3 4 3\n1 4 10\n', '3\r\n2 1\r\n3 2\r\n4 3\r\n'),
        edge('5 5\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n1 5 20\n', '4\r\n2 1\r\n3 2\r\n4 3\r\n5 4\r\n'),
        edge('2 1\n1 2 7\n', '1\r\n2 1\r\n'),
        edge('3 3\n1 2 10\n1 2 2\n2 3 1\n', '2\r\n2 1\r\n3 2\r\n'),
        edge('4 4\n1 2 1\n1 3 5\n2 3 1\n3 4 1\n', '3\r\n2 1\r\n3 2\r\n4 3\r\n'),
        stress('6 7\n1 2 1\n2 3 2\n3 4 3\n4 5 4\n5 6 5\n1 6 30\n2 6 20\n', '5\r\n2 1\r\n3 2\r\n4 3\r\n5 4\r\n6 5\r\n'),
    ]
