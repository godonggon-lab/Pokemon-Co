from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2\n1 1 10\n2 2 20\n3 3 30\n', '30\r\n'),
        edge('4 3\n0 0 5\n1 2 7\n2 1 11\n3 3 13\n', '23\r\n'),
        stress('5 2\n0 5 3\n1 4 4\n2 3 5\n3 2 6\n4 1 7\n', '13\r\n'),
    ]
