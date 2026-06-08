from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\n0 0 0\n', 'SAD\r\n'),
        edge('5 2\n1 4 2 5 1\n', '7\r\n1\r\n'),
        stress('8 3\n5 1 2 3 5 5 1 9\n', '15\r\n1\r\n'),
    ]
