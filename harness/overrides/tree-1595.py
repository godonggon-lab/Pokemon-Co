from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('', '0\r\n'),
        edge('1 2 3\n', '3\r\n'),
        stress('1 2 5\n2 3 7\n2 4 2\n4 5 9\n', '18\r\n'),
    ]
