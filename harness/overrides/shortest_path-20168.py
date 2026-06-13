from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2 1 3 5\n1 2 2\n2 3 3\n', '3\r\n'),
        edge('4 4 1 4 6\n1 2 4\n2 4 4\n1 3 2\n3 4 3\n', '3\r\n'),
        edge('2 1 1 2 4\n1 2 5\n', '-1\r\n'),
        edge('3 3 1 3 10\n1 2 8\n2 3 1\n1 3 6\n', '6\r\n'),
        edge('4 4 1 4 9\n1 2 4\n2 4 4\n1 3 5\n3 4 3\n', '4\r\n'),
        stress('5 6 1 5 10\n1 2 5\n2 5 5\n1 3 2\n3 4 2\n4 5 6\n2 3 1\n', '5\r\n'),
    ]
