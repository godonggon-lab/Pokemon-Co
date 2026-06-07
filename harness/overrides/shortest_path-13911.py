from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4 3\n1 2 3\n2 3 4\n3 4 5\n1 10\n1\n1 10\n4\n', '12\r\n'),
        edge('5 5\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n1 5 10\n1 5\n1\n1 5\n5\n', '8\r\n'),
        stress('6 7\n1 2 1\n2 3 2\n3 4 3\n4 5 4\n5 6 5\n1 6 10\n2 5 2\n2 4\n1 2\n2 4\n5 6\n', '6\r\n'),
    ]
