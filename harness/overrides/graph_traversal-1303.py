from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\nW\n', '1 0\r\n'),
        edge('5 5\nWBWWW\nWWWWW\nBBBBB\nBBBWW\nWWWWW\n', '130 65\r\n'),
        edge('3 2\nWWW\nBBB\n', '9 9\r\n'),
        edge('4 3\nWBWB\nBWBW\nWBWB\n', '6 6\r\n'),
        edge('2 2\nBB\nBB\n', '0 16\r\n'),
        stress('10 10\nWWWWWWWWWW\nWWWWWWWWWW\nWWWWWWWWWW\nWWWWWWWWWW\nWWWWWWWWWW\nBBBBBBBBBB\nBBBBBBBBBB\nBBBBBBBBBB\nBBBBBBBBBB\nBBBBBBBBBB\n', '2500 2500\r\n'),
    ]
