from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3\n1 3\n1 2 5\n2 3 4\n1 3 3\n', '4\r\n'),
        edge('4 2\n1 4\n1 2 10\n3 4 10\n', '0\r\n'),
        stress('5 6\n1 5\n1 2 7\n2 5 3\n1 3 5\n3 4 6\n4 5 4\n2 4 8\n', '4\r\n'),
    ]
