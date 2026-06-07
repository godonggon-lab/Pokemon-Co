from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3\n1 0 1\n0 0 0\n1 0 1\n', '-1\r\n'),
        edge('3 3\n1 1 1\n1 1 1\n1 1 1\n', '0\r\n'),
        stress('5 7\n1 0 0 0 0 0 1\n1 0 0 0 0 0 1\n0 0 0 0 0 0 0\n1 0 0 0 0 0 1\n1 0 0 0 0 0 1\n', '-1\r\n'),
    ]
