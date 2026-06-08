from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n-1 0 1\n', '1\r\n'),
        edge('5\n0 0 0 0 0\n', '10\r\n'),
        edge('6\n-2 -1 0 1 2 3\n', '3\r\n'),
        stress('50\n-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 -10 -9 -8 -7 -6 -5 -4 -3\n', '660\r\n'),
    ]
