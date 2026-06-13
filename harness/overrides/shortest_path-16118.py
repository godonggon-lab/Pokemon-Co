from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2 1\n', '0\r\n'),
        edge('4 4\n1 2 1\n2 3 1\n3 4 1\n1 4 10\n', '1\r\n'),
        edge('3 2\n1 2 1\n2 3 1\n', '1\r\n'),
        edge('3 3\n1 2 10\n1 3 1\n3 2 1\n', '1\r\n'),
        edge('4 4\n1 2 2\n2 4 2\n1 3 1\n3 4 5\n', '1\r\n'),
        stress('5 6\n1 2 3\n1 3 2\n2 4 4\n3 4 1\n4 5 2\n2 5 10\n', '0\r\n'),
    ]
