from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 10\n0 5 3\n5 10 3\n', '6\r\n'),
        edge('3 20\n0 10 5\n10 20 5\n0 20 30\n', '10\r\n'),
        edge('0 7\n', '7\r\n'),
        edge('2 10\n0 10 10\n2 8 2\n', '6\r\n'),
        edge('3 10\n0 5 2\n5 12 1\n7 10 1\n', '5\r\n'),
        stress('4 30\n0 10 8\n8 20 5\n20 30 3\n5 25 10\n', '16\r\n'),
    ]
