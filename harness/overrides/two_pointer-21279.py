from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2\n1 1 10\n2 2 20\n3 3 30\n', '30\r\n'),
        edge('4 3\n0 0 5\n1 2 7\n2 1 11\n3 3 13\n', '23\r\n'),
        edge('1 1\n0 0 7\n', '7\r\n'),
        edge('3 3\n0 2 5\n2 0 6\n2 2 7\n', '18\r\n'),
        edge('4 2\n0 0 1\n0 1 2\n1 0 4\n1 1 8\n', '5\r\n'),
        stress('5 2\n0 5 3\n1 4 4\n2 3 5\n3 2 6\n4 1 7\n', '13\r\n'),
    ]
