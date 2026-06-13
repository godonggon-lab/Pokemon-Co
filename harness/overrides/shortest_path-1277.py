from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 0\n10.0\n0 0\n3 4\n', '5000\r\n'),
        edge('3 1\n5.0\n0 0\n3 4\n6 8\n1 2\n', '5000\r\n'),
        edge('2 1\n1.0\n0 0\n100 100\n1 2\n', '0\r\n'),
        edge('3 0\n5.0\n0 0\n3 4\n6 8\n', '10000\r\n'),
        edge('3 1\n5.0\n0 0\n3 4\n6 8\n1 2\n', '5000\r\n'),
        stress('4 1\n5.5\n0 0\n3 4\n6 8\n10 10\n2 3\n', '9472\r\n'),
    ]
