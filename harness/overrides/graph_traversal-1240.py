from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 2\n1 2 7\n1 2\n2 1\n', '7\r\n7\r\n'),
        edge('4 3\n1 2 3\n2 3 4\n2 4 5\n1 3\n3 4\n1 4\n', '7\r\n9\r\n8\r\n'),
        edge('2 1\n1 2 1\n1 1\n', '0\r\n'),
        edge('3 2\n1 2 10\n1 3 20\n2 3\n3 2\n', '30\r\n30\r\n'),
        edge('4 2\n1 2 1\n2 3 2\n3 4 3\n1 4\n2 2\n', '6\r\n0\r\n'),
        stress('6 4\n1 2 1\n2 3 2\n3 4 3\n4 5 4\n5 6 5\n1 6\n2 5\n3 3\n6 1\n', '15\r\n9\r\n0\r\n15\r\n'),
    ]
