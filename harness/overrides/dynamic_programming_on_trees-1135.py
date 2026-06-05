from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n-1\n', '0\r\n'),
        edge('2\n-1 0\n', '1\r\n'),
        edge('3\n-1 0 1\n', '2\r\n'),
        edge('4\n-1 0 0 0\n', '3\r\n'),
        edge('5\n-1 0 0 1 1\n', '3\r\n'),
        stress('7\n-1 0 0 1 1 2 2\n', '4\r\n'),
    ]
