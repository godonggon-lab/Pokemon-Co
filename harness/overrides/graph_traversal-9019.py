from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1234 3412\n', 'LL\r\n'),
        edge('1\n0 9999\n', 'S\r\n'),
        stress('3\n1 16\n1000 1\n1234 4321\n', 'DDDD\r\nL\r\nSDLSLSSDRS\r\n'),
    ]
