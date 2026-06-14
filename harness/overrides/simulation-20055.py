from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2\n1 2 1 2 1 2\n', '2\r\n'),
        edge('2 3\n1 1 1 1\n', '3\r\n'),
        edge('2 1\n1 1 1 1\n', '1\r\n'),
        edge('2 4\n1 1 1 1\n', '4\r\n'),
        edge('3 3\n3 3 3 3 3 3\n', '8\r\n'),
        stress('4 4\n3 2 1 2 3 2 1 2\n', '6\r\n'),
    ]
