from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\n1 1\n3 2\n', '1\r\n'),
        edge('5 2\n3 3\n1 2\n5 5\n', '1 4\r\n'),
        edge('1 1\n1 1\n1 1\n', '0\r\n'),
        edge('4 2\n1 1\n2 3\n4 4\n', '1 2\r\n'),
        edge('8 2\n1 1\n8 8\n4 5\n', '6 3\r\n'),
        stress('8 3\n1 1\n8 8\n4 5\n2 3\n', '6 3 1\r\n'),
    ]
