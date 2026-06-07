from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 0\n', '1\r\n'),
        edge('3 2\n1 2\n2 3\n', '3\r\n'),
        stress('5 5\n1 2\n2 3\n3 4\n4 5\n2 5\n', '5\r\n'),
    ]
