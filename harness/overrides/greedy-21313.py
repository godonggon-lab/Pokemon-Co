from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n', '1\r\n'),
        edge('4\n', '1 2 1 2\r\n'),
        stress('7\n', '1 2 1 2 1 2 3\r\n'),
    ]
