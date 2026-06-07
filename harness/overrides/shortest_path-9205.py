from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n0\n0 0\n800 0\n', 'happy\r\n'),
        edge('2\n1\n0 0\n1000 0\n2000 0\n1\n0 0\n1000 1000\n2000 2000\n', 'happy\r\nsad\r\n'),
        stress('1\n5\n0 0\n800 0\n1600 0\n2400 0\n3200 0\n4000 0\n4800 0\n', 'happy\r\n'),
    ]
