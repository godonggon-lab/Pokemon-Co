from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1 1\n1 1\n', '1\r\n'),
        edge('3 3 3\n1 1\n1 2\n3 3\n', '2\r\n'),
        edge('4 5 6\n1 1\n1 2\n2 2\n4 4\n4 5\n3 5\n', '3\r\n'),
        stress('10 10 20\n1 1\n1 2\n2 3\n2 4\n3 5\n3 6\n4 7\n4 8\n5 9\n5 10\n6 1\n6 2\n7 3\n7 4\n8 5\n8 6\n9 7\n9 8\n10 9\n10 10\n', '2\r\n'),
    ]
