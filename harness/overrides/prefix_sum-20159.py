from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4\n1 2 3 4\n', '6\r\n'),
        edge('6\n10 1 10 1 10 1\n', '30\r\n'),
        edge('2\n5 7\n', '7\r\n'),
        edge('4\n10 1 1 10\n', '20\r\n'),
        edge('6\n1 1 1 1 1 1\n', '3\r\n'),
        stress('8\n5 3 8 2 7 4 6 1\n', '26\r\n'),
    ]
