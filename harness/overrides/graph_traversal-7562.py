from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n8\n0 0\n7 0\n', '5\r\n'),
        edge('2\n4\n0 0\n0 0\n10\n0 0\n9 9\n', '0\r\n6\r\n'),
        edge('1\n4\n0 0\n1 2\n', '1\r\n'),
        edge('1\n5\n0 0\n4 4\n', '4\r\n'),
        edge('1\n6\n0 0\n5 5\n', '4\r\n'),
        stress('1\n300\n0 0\n299 299\n', '200\r\n'),
    ]
