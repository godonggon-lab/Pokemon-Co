from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0\n', '0\r\n'),
        edge('3\n2\n1 2\n2 3\n', '0\r\n0\r\n0\r\n'),
        stress('5\n4\n1 2\n3 2\n4 5\n5 3\n', '3\r\n0\r\n1\r\n1\r\n1\r\n'),
    ]
