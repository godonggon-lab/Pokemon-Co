from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 3 1 20\n', '4\r\n'),
        edge('5 7 10 10\n', '0\r\n'),
        edge('3 4 100 1\n', '25\r\n'),
        stress('7 11 0 100000\n', '12\r\n'),
    ]
