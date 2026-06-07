from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4\n4\n1 2 2\n2 4 3\n1 3 10\n3 4 1\n1 4\n', '5\r\n3\r\n1 2 4\r\n'),
        edge('5\n6\n1 2 2\n2 3 2\n3 5 2\n1 4 10\n4 5 1\n2 5 9\n1 5\n', '6\r\n4\r\n1 2 3 5\r\n'),
        stress('6\n7\n1 2 1\n2 3 1\n3 6 1\n1 4 5\n4 5 5\n5 6 5\n2 5 2\n1 6\n', '3\r\n4\r\n1 2 3 6\r\n'),
    ]
