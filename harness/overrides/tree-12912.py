from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n0 1 2\n1 2 3\n', '5\r\n'),
        edge('4\n0 1 1\n1 2 1\n2 3 1\n', '3\r\n'),
        stress('5\n0 1 4\n1 2 2\n1 3 3\n3 4 5\n', '14\r\n'),
    ]
