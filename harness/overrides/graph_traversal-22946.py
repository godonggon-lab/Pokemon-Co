from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n0 0 10\n0 0 5\n0 0 2\n', '2\r\n'),
        edge('4\n0 0 20\n-5 0 3\n5 0 3\n0 0 1\n', '2\r\n'),
        edge('1\n0 0 10\n', '0\r\n'),
        edge('2\n0 0 10\n100 100 1\n', '2\r\n'),
        edge('3\n0 0 10\n0 0 9\n0 0 8\n', '2\r\n'),
        stress('5\n0 0 30\n0 0 20\n0 0 10\n-20 0 5\n20 0 5\n', '3\r\n'),
    ]
