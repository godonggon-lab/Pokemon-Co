from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1 2\n1 0\n0 0\n1\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n', '1\r\n'),
        edge('3 2 3\n1 0 0\n0 0 0\n0 0 2\n1 2\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n', '2\r\n'),
        edge('2 1 1\n1 0\n0 0\n1\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n', '1\r\n'),
        edge('2 1 3\n0 0\n0 1\n1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n4 3 2 1\n', '1\r\n'),
        edge('3 1 2\n0 0 0\n0 1 0\n0 0 0\n1\n2 3 4 1\n2 3 4 1\n2 3 4 1\n2 3 4 1\n', '1\r\n'),
        stress('4 3 3\n1 0 0 2\n0 0 0 0\n0 0 0 0\n3 0 0 0\n1 2 3\n1 2 3 4\n2 1 3 4\n3 4 1 2\n4 3 2 1\n1 2 3 4\n2 1 3 4\n3 4 1 2\n4 3 2 1\n1 2 3 4\n2 1 3 4\n3 4 1 2\n4 3 2 1\n', '-1\r\n'),
    ]
