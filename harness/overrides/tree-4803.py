from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 0\n0 0\n', 'Case 1: There is one tree.\r\n'),
        edge('3 3\n1 2\n2 3\n3 1\n0 0\n', 'Case 1: No trees.\r\n'),
        stress('5 3\n1 2\n2 3\n4 5\n4 4\n1 2\n2 3\n3 4\n4 1\n0 0\n', 'Case 1: A forest of 2 trees.\r\nCase 2: No trees.\r\n'),
    ]
