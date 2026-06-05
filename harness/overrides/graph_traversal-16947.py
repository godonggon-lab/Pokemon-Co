from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n1 2\n2 3\n3 1\n', '0 0 0\r\n'),
        stress('6\n1 2\n2 3\n3 1\n3 4\n4 5\n5 6\n', '0 0 0 1 2 3\r\n'),
    ]
