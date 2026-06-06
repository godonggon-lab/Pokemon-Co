from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\nB\nW\n', '1\r\n'),
        edge('1\n4\nBBBB\nWWWW\n', '4\r\n'),
        edge('1\n4\nBWBW\nWBWB\n', '2\r\n'),
        edge('2\n5\nBBBBB\nBBBBB\n6\nBWBWBW\nWWBBWB\n', '0\r\n2\r\n'),
        stress('1\n100\nBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBW\nWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWBWB\n', '50\r\n'),
    ]
