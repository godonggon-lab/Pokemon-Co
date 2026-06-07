from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2 3\n', '-1\r\n'),
        edge('3 3\n1 2 1\n2 3 1\n3 1 1\n', '3\r\n'),
        stress('4 5\n1 2 4\n2 3 5\n3 1 6\n2 4 1\n4 2 1\n', '2\r\n'),
    ]
