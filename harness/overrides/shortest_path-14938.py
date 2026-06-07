from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5 5 5\n5 7 8 2 3\n1 2 3\n1 3 4\n2 4 5\n3 4 2\n4 5 3\n', '20\r\n'),
        edge('3 0 1\n1 2 3\n1 2 1\n', '3\r\n'),
        stress('6 7 7\n1 4 2 7 3 5\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n5 6 2\n1 6 10\n2 5 3\n', '22\r\n'),
    ]
