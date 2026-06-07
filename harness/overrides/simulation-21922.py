from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n9\n', '1\r\n'),
        edge('3 3\n9 0 0\n0 1 0\n0 0 0\n', '5\r\n'),
        stress('4 5\n9 0 2 0 0\n0 3 0 4 0\n0 0 0 0 9\n1 0 2 0 0\n', '13\r\n'),
    ]
