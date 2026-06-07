from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3\n1 2 1\n2 3 2\n', '2\r\n'),
        edge('5\n1 2 3\n1 3 4\n3 4 5\n3 5 6\n', '12\r\n'),
        stress('6\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n5 6 2\n', '8\r\n'),
    ]
