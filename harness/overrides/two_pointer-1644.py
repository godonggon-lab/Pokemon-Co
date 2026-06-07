from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n', '0\r\n'),
        edge('2\n', '1\r\n'),
        edge('3\n', '1\r\n'),
        edge('41\n', '3\r\n'),
        edge('53\n', '2\r\n'),
        stress('4000\n', '1\r\n'),
    ]
