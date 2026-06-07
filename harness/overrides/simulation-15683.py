from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3\n0 0 0\n0 1 0\n0 0 0\n', '7\r\n'),
        edge('4 6\n0 0 0 0 0 0\n0 2 0 6 0 0\n0 0 0 0 3 0\n0 0 0 0 0 0\n', '13\r\n'),
        stress('5 5\n0 6 0 0 0\n0 1 0 2 0\n0 0 6 0 0\n0 3 0 4 0\n0 0 0 0 5\n', '3\r\n'),
    ]
