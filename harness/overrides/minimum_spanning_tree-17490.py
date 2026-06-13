from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4 1 10\n1 2 3 4\n1 2\n', 'YES\r\n'),
        edge('5 2 7\n3 4 5 6 7\n1 2\n3 4\n', 'YES\r\n'),
        edge('3 0 0\n5 6 7\n', 'YES\r\n'),
        edge('3 2 4\n5 1 5\n1 2\n2 3\n', 'NO\r\n'),
        edge('4 2 2\n5 5 5 5\n1 2\n3 4\n', 'NO\r\n'),
        stress('6 3 8\n5 1 4 2 6 3\n1 2\n2 3\n5 6\n', 'YES\r\n'),
    ]
