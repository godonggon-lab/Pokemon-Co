from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 2 2 3 0 0\n-1 -1\n', 'Case 1 is a tree.\r\n'),
        edge('1 2 3 2 0 0\n-1 -1\n', 'Case 1 is not a tree.\r\n'),
        edge('0 0\n-1 -1\n', 'Case 1 is a tree.\r\n'),
        edge('1 2 0 0\n-1 -1\n', 'Case 1 is a tree.\r\n'),
        edge('1 3 2 3 0 0\n-1 -1\n', 'Case 1 is not a tree.\r\n'),
        stress('0 0\n1 2 2 3 3 1 0 0\n-1 -1\n', 'Case 1 is a tree.\r\nCase 2 is not a tree.\r\n'),
    ]
