from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4 4\n1 2\n2 4\n1 3\n3 4\n1 4\n', '4\r\n'),
        edge('5 5\n1 2\n2 5\n1 3\n3 4\n4 5\n1 5\n', '5\r\n'),
        edge('2 1\n1 2\n1 2\n', '2\r\n'),
        edge('3 3\n1 2\n2 3\n1 3\n1 3\n', '2\r\n'),
        edge('4 4\n1 2\n2 4\n1 3\n3 4\n1 4\n', '4\r\n'),
        stress('6 7\n1 2\n2 6\n1 3\n3 4\n4 6\n2 3\n5 6\n1 6\n', '5\r\n'),
    ]
