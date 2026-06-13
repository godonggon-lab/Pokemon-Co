from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1\n2 0 0\n0 1 0\n0 0 0\n', '4\r\n'),
        edge('3 1\n2 1 0\n1 1 0\n0 0 0\n', '-1\r\n'),
        edge('2 1\n2 2\n2 2\n', '0\r\n'),
        edge('3 1\n2 0 0\n0 0 0\n0 0 0\n', '4\r\n'),
        edge('3 1\n2 1 0\n1 1 1\n0 0 0\n', '-1\r\n'),
        stress('5 2\n2 0 0 1 2\n0 1 0 0 0\n0 0 0 1 0\n1 0 1 0 0\n2 0 0 0 0\n', '5\r\n'),
    ]
