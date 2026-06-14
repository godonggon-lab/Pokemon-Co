from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 1\n1 1\n', '16\r\n'),
        edge('3 2\n1 0 2\n1 -1 2\n0 2 2\n', '36\r\n'),
        edge('2 1\n1 -1\n-1 1\n', '0\r\n'),
        edge('2 2\n1 1\n2 2\n', '4\r\n'),
        edge('3 1\n1 0 1\n-1 -1 -1\n1 0 1\n', '9\r\n'),
        stress('5 3\n1 0 2 2 3\n1 -1 0 2 3\n1 1 2 -1 3\n0 2 2 3 3\n1 0 0 3 3\n', '121\r\n'),
    ]
