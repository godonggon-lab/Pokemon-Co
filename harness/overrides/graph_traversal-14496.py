from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 2\n2 1\n1 2\n', '1\r\n'),
        edge('1 3\n3 1\n1 2\n', '-1\r\n'),
        edge('1 1\n1 0\n', '0\r\n'),
        edge('1 4\n4 1\n1 2\n', '-1\r\n'),
        edge('1 4\n4 3\n1 2\n2 3\n3 4\n', '3\r\n'),
        stress('1 5\n5 5\n1 2\n2 3\n3 5\n1 4\n4 5\n', '2\r\n'),
    ]
