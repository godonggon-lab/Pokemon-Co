from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2 3\n', '3\r\n'),
        edge('3 3\n1 2 4\n2 3 -10\n3 2 3\n', '-1\r\n'),
        edge('3 1\n1 2 5\n', '5\r\n-1\r\n'),
        edge('3 3\n1 2 3\n2 3 -2\n1 3 5\n', '3\r\n1\r\n'),
        edge('4 3\n2 3 -5\n3 2 1\n1 4 7\n', '-1\r\n-1\r\n7\r\n'),
        stress('4 4\n1 2 5\n2 3 2\n1 4 20\n3 4 -1\n', '5\r\n7\r\n6\r\n'),
    ]
