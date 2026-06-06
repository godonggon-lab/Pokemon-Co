from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n10\n1\n', '10\r\n'),
        edge('3\n1 2 3\n1 2 3\n', '14\r\n'),
        edge('3\n10 10 10\n3 2 1\n', '38\r\n'),
        edge('5\n1 2 3 4 5\n5 4 3 2 1\n', '55\r\n'),
        edge('6\n10 1 10 1 10 1\n1 10 2 9 3 8\n', '151\r\n'),
        stress('8\n1 2 3 4 5 6 7 8\n8 7 6 5 4 3 2 1\n', '204\r\n'),
    ]
