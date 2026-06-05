from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3 1 1 0\n1 1\n3 3\n', '4\r\n'),
        edge('4 4 2 2 1\n2 2\n1 1\n3 3\n', '-1\r\n'),
        stress('5 5 2 3 2\n2 2\n4 4\n1 1\n3 3\n', '-1\r\n'),
    ]
