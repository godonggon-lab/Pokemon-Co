from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n0 0\n', 'stable\r\n'),
        edge('3 1\n0 3 0\n', 'unstable\r\n'),
        edge('1 0\n0\n', 'stable\r\n'),
        edge('3 1\n0 1 2\n', 'unstable\r\n'),
        edge('4 2\n0 4 4 0\n', 'unstable\r\n'),
        stress('5 3\n1 3 5 7 9\n', 'unstable\r\n'),
    ]
