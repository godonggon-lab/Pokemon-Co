from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('', '0\r\n'),
        edge('1 2 3\n', '3\r\n'),
        edge('1 2 5\n2 3 5\n', '10\r\n'),
        edge('1 2 1\n1 3 2\n1 4 3\n', '5\r\n'),
        edge('10 20 7\n20 30 8\n30 40 9\n', '24\r\n'),
        stress('1 2 5\n2 3 7\n2 4 2\n4 5 9\n', '18\r\n'),
    ]
