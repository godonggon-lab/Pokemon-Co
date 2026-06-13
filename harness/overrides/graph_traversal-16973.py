from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3\n0 0 0\n0 0 0\n0 0 0\n1 1 1 1 3 3\n', '4\r\n'),
        edge('4 4\n0 0 0 0\n0 1 0 0\n0 0 0 0\n0 0 0 0\n2 2 1 1 3 3\n', '-1\r\n'),
        edge('2 2\n0 0\n0 0\n1 1 1 1 1 1\n', '0\r\n'),
        edge('2 2\n0 0\n0 0\n1 1 1 1 2 2\n', '2\r\n'),
        edge('3 3\n0 0 0\n0 0 0\n0 0 0\n2 2 1 1 2 2\n', '2\r\n'),
        stress('5 5\n0 0 0 0 0\n0 1 0 1 0\n0 0 0 0 0\n0 1 0 0 0\n0 0 0 0 0\n2 2 1 1 4 4\n', '-1\r\n'),
    ]
