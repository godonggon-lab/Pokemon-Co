from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n3 10\n', '7\r\n'),
        edge('2\n5 5\n1 6\n', '0\r\n'),
        edge('3\n3 8\n2 7\n4 10\n', '1\r\n'),
        edge('4\n4 20\n10 15\n2 12\n1 11\n', '2\r\n'),
        edge('3\n10 5\n1 20\n1 21\n', '-1\r\n'),
        stress('20\n1 100\n2 99\n3 98\n4 97\n5 96\n1 95\n2 94\n3 93\n4 92\n5 91\n1 90\n2 89\n3 88\n4 87\n5 86\n1 85\n2 84\n3 83\n4 82\n5 81\n', '40\r\n'),
    ]
