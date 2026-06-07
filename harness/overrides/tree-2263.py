from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n1\n', '1\r\n'),
        edge('3\n2 1 3\n2 3 1\n', '1 2 3\r\n'),
        stress('7\n4 2 5 1 6 3 7\n4 5 2 6 7 3 1\n', '1 2 4 5 3 6 7\r\n'),
    ]
