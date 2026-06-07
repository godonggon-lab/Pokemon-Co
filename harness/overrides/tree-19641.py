from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n1 2 -1\n2 1 3 -1\n3 2 -1\n1\n', '1 1 6\r\n2 2 5\r\n3 3 4\r\n'),
        edge('5\n1 2 3 -1\n2 1 4 -1\n3 1 5 -1\n4 2 -1\n5 3 -1\n1\n', '1 1 10\r\n2 2 5\r\n3 6 9\r\n4 3 4\r\n5 7 8\r\n'),
        stress('6\n1 2 3 -1\n2 1 4 5 -1\n3 1 6 -1\n4 2 -1\n5 2 -1\n6 3 -1\n2\n', '1 2 7\r\n2 1 12\r\n3 3 6\r\n4 8 9\r\n5 10 11\r\n6 4 5\r\n'),
    ]
