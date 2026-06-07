from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2\n', '1\r\n'),
        edge('5 5\n1 3\n1 4\n4 5\n4 3\n3 2\n', '3\r\n'),
        stress('6 7\n1 2\n2 3\n3 4\n4 5\n5 6\n1 6\n2 5\n', '2\r\n'),
    ]
