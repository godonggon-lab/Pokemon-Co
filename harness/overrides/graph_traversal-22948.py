from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n1 0 10\n2 0 5\n3 0 2\n2 3\n', '2\r\n2 3\r\n'),
        edge('4\n1 0 20\n2 -5 5\n3 5 5\n4 0 1\n2 3\n', '3\r\n2 1 3\r\n'),
        edge('1\n7 0 10\n0 0\n', '0\r\n\r\n'),
        edge('2\n1 0 10\n2 100 1\n0 0\n', '0\r\n\r\n'),
        edge('3\n1 0 10\n2 0 9\n3 0 8\n1 3\n', '3\r\n1 2 3\r\n'),
        stress('5\n1 0 30\n2 -10 8\n3 10 8\n4 -10 2\n5 10 2\n4 5\n', '5\r\n4 2 1 3 5\r\n'),
    ]
