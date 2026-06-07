from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0\n', '1\r\n'),
        edge('5\n1\n2 4\n', '3\r\n'),
        stress('8\n3\n1 3\n5 8\n2 6\n', '1\r\n'),
    ]
