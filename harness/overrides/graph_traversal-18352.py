from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2 1 1\n1 2\n2 3\n', '2\r\n'),
        edge('3 1 2 1\n1 2\n', '-1\r\n'),
        edge('1 0 0 1\n', '1\r\n'),
        edge('4 3 1 1\n1 2\n1 3\n1 4\n', '2\r\n3\r\n4\r\n'),
        edge('4 2 2 1\n1 2\n2 3\n', '3\r\n'),
        stress('5 5 2 1\n1 2\n1 3\n2 4\n3 4\n4 5\n', '4\r\n'),
    ]
