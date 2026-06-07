from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n5 4 2\n1 2 3\n1 2 1\n2 3 1\n3 4 1\n3 5 2\n4\n5\n', '4 5\r\n'),
        stress('1\n4 4 2\n1 2 3\n1 2 1\n2 3 1\n3 4 1\n1 4 10\n3\n4\n', '3 4\r\n'),
    ]
