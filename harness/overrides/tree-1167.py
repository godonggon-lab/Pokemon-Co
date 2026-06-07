from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 -1\n', '0\r\n'),
        edge('3\n1 2 3 -1\n2 1 3 3 4 -1\n3 2 4 -1\n', '7\r\n'),
        stress('5\n1 2 1 3 2 -1\n2 1 1 4 3 -1\n3 1 2 -1\n4 2 3 5 4 -1\n5 4 4 -1\n', '10\r\n'),
    ]
