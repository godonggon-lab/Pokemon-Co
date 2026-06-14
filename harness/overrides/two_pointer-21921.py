from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\n0 0 0\n', 'SAD\r\n'),
        edge('5 2\n1 4 2 5 1\n', '7\r\n1\r\n'),
        edge('1 1\n9\n', '9\r\n1\r\n'),
        edge('4 2\n1 2 2 1\n', '4\r\n1\r\n'),
        edge('5 3\n1 1 1 1 1\n', '3\r\n3\r\n'),
        stress('8 3\n5 1 2 3 5 5 1 9\n', '15\r\n1\r\n'),
    ]
