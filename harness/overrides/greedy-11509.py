from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n5\n', '1\r\n'),
        edge('5\n5 4 3 2 1\n', '1\r\n'),
        edge('5\n1 2 3 4 5\n', '5\r\n'),
        edge('7\n2 1 5 4 3 2 1\n', '2\r\n'),
        edge('8\n3 3 3 2 2 1 1 1\n', '4\r\n'),
        stress('30\n1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10\n', '12\r\n'),
    ]
