from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 10\n1\n1 2 7\n', '7\r\n'),
        edge('4 40\n6\n3 4 20\n1 2 10\n1 3 20\n2 4 30\n2 3 10\n1 4 20\n', '70\r\n'),
        edge('3 10\n2\n1 2 10\n2 3 10\n', '20\r\n'),
        edge('3 10\n2\n1 3 10\n1 2 10\n', '10\r\n'),
        edge('4 5\n4\n1 4 5\n1 2 5\n2 3 5\n3 4 5\n', '15\r\n'),
        stress('5 15\n7\n1 3 10\n1 4 10\n2 5 10\n2 3 5\n3 5 8\n1 2 7\n4 5 7\n', '35\r\n'),
    ]
