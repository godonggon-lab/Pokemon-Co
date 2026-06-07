from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n2 2\n1\n2\n3 4\n', '6\r\n'),
        edge('1\n1 3\n5 6\n\n', '11\r\n'),
        stress('1\n3 3\n1 2\n3 4\n5 6\n7 8 9\n1 2 3\n4 5 6\n', '23\r\n'),
    ]
