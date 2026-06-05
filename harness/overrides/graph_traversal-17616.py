from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 0 1\n', '1 1\r\n'),
        edge('3 2 2\n1 2\n2 3\n', '2 2\r\n'),
        stress('5 5 3\n1 3\n2 3\n3 4\n3 5\n1 5\n', '3 3\r\n'),
    ]
