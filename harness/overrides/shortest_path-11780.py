from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n3\n1 2 2\n2 3 3\n1 3 10\n', '0 2 5\r\n0 0 3\r\n0 0 0\r\n0\r\n2 1 2\r\n3 1 2 3\r\n0\r\n0\r\n2 2 3\r\n0\r\n0\r\n0\r\n'),
        edge('4\n5\n1 2 1\n2 3 1\n3 4 1\n1 4 10\n2 4 5\n', '0 1 2 3\r\n0 0 1 2\r\n0 0 0 1\r\n0 0 0 0\r\n0\r\n2 1 2\r\n3 1 2 3\r\n4 1 2 3 4\r\n0\r\n0\r\n2 2 3\r\n3 2 3 4\r\n0\r\n0\r\n0\r\n2 3 4\r\n0\r\n0\r\n0\r\n0\r\n'),
        stress('5\n6\n1 2 2\n2 5 2\n1 3 5\n3 4 5\n4 5 5\n2 3 1\n', '0 2 3 8 4\r\n0 0 1 6 2\r\n0 0 0 5 10\r\n0 0 0 0 5\r\n0 0 0 0 0\r\n0\r\n2 1 2\r\n3 1 2 3\r\n4 1 2 3 4\r\n3 1 2 5\r\n0\r\n0\r\n2 2 3\r\n3 2 3 4\r\n2 2 5\r\n0\r\n0\r\n0\r\n2 3 4\r\n3 3 4 5\r\n0\r\n0\r\n0\r\n0\r\n2 4 5\r\n0\r\n0\r\n0\r\n0\r\n0\r\n'),
    ]
