from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n', 'No\r\n'),
        edge('3\n1 2\n1 3\n', 'No\r\n'),
        stress('6\n1 2\n2 3\n3 4\n2 5\n5 6\n', 'No\r\n'),
    ]
