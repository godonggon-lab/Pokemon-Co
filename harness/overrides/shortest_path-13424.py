from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n2 1\n1 2 5\n2\n1 2\n', '1\r\n'),
        stress('1\n4 4\n1 2 2\n2 3 2\n3 4 2\n1 4 10\n3\n1 3 4\n', '3\r\n'),
    ]
