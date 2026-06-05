from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2\n1 2\n2 3\n3\n', '2\r\n'),
        edge('5 4\n1 3\n2 3\n3 4\n4 5\n5\n', '4\r\n'),
        stress('7 7\n1 4\n2 4\n3 5\n4 6\n5 6\n6 7\n2 5\n7\n', '6\r\n'),
    ]
