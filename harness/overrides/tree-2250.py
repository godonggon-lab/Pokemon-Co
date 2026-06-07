from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 -1 -1\n', '1 1\r\n'),
        edge('3\n1 2 3\n2 -1 -1\n3 -1 -1\n', '2 3\r\n'),
        stress('7\n1 2 3\n2 4 5\n3 6 7\n4 -1 -1\n5 -1 -1\n6 -1 -1\n7 -1 -1\n', '3 7\r\n'),
    ]
