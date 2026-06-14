from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4 1\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n1 1 1\n', '-1\r\n'),
        edge('4 4\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n1 1 1\n1 2 1\n1 3 1\n1 4 1\n', '1\r\n'),
        edge('4 1\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n1 1 2\n', '-1\r\n'),
        edge('4 1\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n1 4 1\n', '-1\r\n'),
        edge('4 4\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n2 1 1\n2 2 1\n2 3 1\n2 4 1\n', '1\r\n'),
        stress('5 4\n0 1 2 0 0\n0 0 0 0 0\n0 2 1 0 0\n0 0 0 0 0\n0 0 0 1 0\n1 1 1\n2 2 2\n3 3 3\n4 4 4\n', '-1\r\n'),
    ]
