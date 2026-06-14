from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1 0 0\n', '0\r\n2\r\n'),
        edge('3\n1 0 0\n2 1 1\n3 2 2\n', '1\r\n6\r\n'),
        edge('1\n2 0 0\n', '0\r\n4\r\n'),
        edge('1\n3 0 1\n', '0\r\n4\r\n'),
        edge('2\n1 0 0\n1 1 0\n', '0\r\n4\r\n'),
        stress('5\n1 0 0\n1 0 1\n2 1 1\n3 2 2\n1 3 3\n', '1\r\n10\r\n'),
    ]
