from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n3\n3 2 1\n0\n', '3 2 1\r\n'),
        edge('1\n5\n5 4 3 2 1\n2\n2 4\n3 4\n', '5 3 2 4 1\r\n'),
        edge('1\n1\n1\n0\n', '1\r\n'),
        edge('1\n2\n1 2\n1\n1 2\n', '2 1\r\n'),
        edge('1\n3\n1 2 3\n2\n1 2\n2 3\n', 'IMPOSSIBLE\r\n'),
        stress('2\n4\n1 2 3 4\n1\n1 2\n3\n1 2 3\n3\n1 2\n2 3\n1 3\n', '2 1 3 4\r\n3 2 1\r\n'),
    ]
