from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 1\n1 2 1\n2 1 3\n3 3 3\n', '0\r\n'),
        edge('2 2 5\n1 1 1\n1 1 1\n1 1 1\n', '-1\r\n'),
        stress('3 3 7\n1 2 3\n3 2 1\n1 1 1\n', '44\r\n'),
    ]
