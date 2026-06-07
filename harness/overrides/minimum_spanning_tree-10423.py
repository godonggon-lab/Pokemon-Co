from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2 1\n1\n1 2 5\n2 3 7\n', '12\r\n'),
        edge('4 4 2\n1 4\n1 2 3\n2 3 4\n3 4 5\n1 3 10\n', '7\r\n'),
        stress('6 8 2\n1 6\n1 2 4\n2 3 2\n3 4 7\n4 5 1\n5 6 3\n2 5 6\n1 4 9\n3 6 8\n', '10\r\n'),
    ]
