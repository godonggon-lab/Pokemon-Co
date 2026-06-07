from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1 1 1\n1 1\n2 3\n', 'YES\r\n'),
        edge('3 1 1 1\n1 1\n1 1\n', 'NO\r\n'),
        edge('5 1 2 2\n3 3\n1 2\n5 5\n', 'NO\r\n'),
        edge('5 2 2 1\n1 1\n5 5\n2 3\n4 3\n', 'YES\r\n'),
        edge('6 2 2 2\n1 1\n3 3\n2 2\n5 4\n', 'YES\r\n'),
        stress('8 3 3 3\n1 1\n4 4\n8 8\n2 3\n6 5\n7 7\n', 'YES\r\n'),
    ]
