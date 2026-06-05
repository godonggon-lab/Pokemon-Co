from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\n1\n10 20\n', '200\r\n'),
        edge('3\n1 1\n10 20 30\n', '300\r\n'),
        edge('3\n1 2\n10 20 30\n', '600\r\n'),
        edge('5\n1 1 2 2\n3 5 7 11 13\n', '86\r\n'),
        edge('6\n1 1 2 2 3\n9 1 8 2 7 3\n', '79\r\n'),
        stress('10\n1 1 2 2 3 3 4 4 5\n1 4 7 10 13 16 19 22 25 28\n', '751\r\n'),
    ]
