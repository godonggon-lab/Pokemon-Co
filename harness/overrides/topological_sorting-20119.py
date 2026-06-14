from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2\n1 1 2\n1 2 3\n1\n1\n', '3\r\n1 2 3\r\n'),
        edge('4 3\n2 1 2 3\n1 3 4\n1 2 4\n2\n1 2\n', '4\r\n1 2 3 4\r\n'),
        edge('3 1\n2 1 2 3\n1\n1\n', '1\r\n1\r\n'),
        edge('3 1\n2 1 2 3\n1\n3\n', '1\r\n3\r\n'),
        edge('4 3\n1 1 3\n1 2 3\n1 3 4\n2\n1 2\n', '4\r\n1 2 3 4\r\n'),
        stress('5 4\n2 1 2 3\n1 3 4\n2 2 4 5\n1 1 5\n1\n1\n', '2\r\n1 5\r\n'),
    ]
