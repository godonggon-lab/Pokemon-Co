from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 0 2\nWWW\n', '3\r\n'),
        edge('5 1 2\nBWWBW\n', '4\r\n'),
        edge('4 0 4\nWWWW\n', '4\r\n'),
        edge('5 2 1\nBBWBW\n', '4\r\n'),
        edge('4 0 1\nBBBB\n', '0\r\n'),
        stress('10 2 4\nWBWBWWBBWW\n', '6\r\n'),
    ]
