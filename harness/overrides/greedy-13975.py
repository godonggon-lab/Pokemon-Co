from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n10\n', '0\r\n'),
        edge('2\n4\n40 30 30 50\n3\n1 1 1\n', '300\r\n5\r\n'),
        stress('1\n30\n1 18 35 52 69 86 3 20 37 54 71 88 5 22 39 56 73 90 7 24 41 58 75 92 9 26 43 60 77 94\n', '6568\r\n'),
    ]
