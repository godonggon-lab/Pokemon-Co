from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\n1 2\n-1 -1\n', '1 2\r\n1 2\r\n'),
        edge('4\n1 2\n2 3\n3 4\n-1 -1\n', '2 2\r\n2 3\r\n'),
        stress('5\n1 2\n1 3\n2 4\n3 5\n4 5\n-1 -1\n', '2 5\r\n1 2 3 4 5\r\n'),
    ]
