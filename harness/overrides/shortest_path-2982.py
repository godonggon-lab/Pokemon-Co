from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 2\n1 3 0 2\n1 2\n1 2 3\n2 3 4\n', '10\r\n'),
        edge('4 4\n1 4 2 3\n1 2 3\n1 2 3\n2 3 3\n3 4 3\n1 4 10\n', '10\r\n'),
        edge('2 1\n1 2 10 2\n1 2\n1 2 5\n', '5\r\n'),
        edge('3 3\n1 3 10 2\n1 2\n1 2 3\n2 3 3\n1 3 10\n', '6\r\n'),
        edge('4 4\n1 4 0 3\n2 3 4\n1 2 2\n2 3 2\n3 4 2\n1 4 20\n', '6\r\n'),
        stress('5 6\n1 5 1 4\n1 2 3 4\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n1 5 20\n2 5 5\n', '8\r\n'),
    ]
