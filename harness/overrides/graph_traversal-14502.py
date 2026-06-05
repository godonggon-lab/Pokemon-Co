from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3\n2 0 0\n0 0 0\n0 0 0\n', '5\r\n'),
        edge('3 3\n2 1 0\n1 1 0\n0 0 0\n', '2\r\n'),
        edge('3 3\n2 0 2\n0 0 0\n2 0 2\n', '0\r\n'),
        edge('4 4\n2 0 0 0\n0 1 1 0\n0 1 0 0\n0 0 0 2\n', '4\r\n'),
        edge('4 5\n2 0 0 0 0\n0 1 1 1 0\n0 1 0 0 0\n0 0 0 1 2\n', '10\r\n'),
        stress('5 5\n2 0 0 0 0\n0 1 1 1 0\n0 1 0 0 0\n0 1 0 1 0\n0 0 0 1 2\n', '13\r\n'),
    ]
