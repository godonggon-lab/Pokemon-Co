from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 3\n1 2 5\n', '2\r\n'),
        edge('4 2\n1 2 2\n2 3 3\n3 4 4\n', '5\r\n'),
        stress('6 4\n1 2 3\n2 3 4\n2 4 5\n4 5 6\n5 6 7\n', '6\r\n'),
    ]
