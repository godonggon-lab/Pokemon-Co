from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2\n3\n1 2\n2 1\n1 1\n', '-1\r\n1\r\n0\r\n'),
        edge('4 3\n1 2\n2 3\n4 3\n3\n1 3\n4 1\n3 4\n', '-1\r\n0\r\n1\r\n'),
        edge('3 0\n3\n1 2\n2 3\n3 1\n', '0\r\n0\r\n0\r\n'),
        edge('3 2\n1 2\n1 3\n3\n2 3\n2 1\n1 3\n', '0\r\n1\r\n-1\r\n'),
        edge('4 4\n1 2\n2 3\n3 4\n1 4\n3\n1 4\n4 1\n2 4\n', '-1\r\n1\r\n-1\r\n'),
        stress('5 4\n1 2\n2 3\n3 4\n5 4\n4\n1 4\n5 2\n2 5\n3 1\n', '-1\r\n0\r\n0\r\n1\r\n'),
    ]
