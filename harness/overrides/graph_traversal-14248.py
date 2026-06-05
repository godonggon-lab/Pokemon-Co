from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n1\n', '1\r\n'),
        edge('5\n1 2 1 2 1\n3\n', '3\r\n'),
        edge('5\n10 10 10 10 10\n1\n', '1\r\n'),
        stress('30\n1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5\n15\n', '6\r\n'),
    ]
