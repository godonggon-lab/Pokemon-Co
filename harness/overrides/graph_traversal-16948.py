from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n0 0 0 0\n', '0\r\n'),
        edge('3\n0 0 1 1\n', '-1\r\n'),
        edge('5\n0 0 2 1\n', '1\r\n'),
        edge('5\n0 0 4 2\n', '2\r\n'),
        edge('7\n0 0 6 0\n', '-1\r\n'),
        stress('7\n6 6 0 1\n', '4\r\n'),
    ]
