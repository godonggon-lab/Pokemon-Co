from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6\n', '0\r\n'),
        edge('1 1 1 2 1 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6\n', '0\r\n'),
        stress('1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6\n', '0\r\n'),
    ]
