from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n3 2 1\n1 2 2\n2 3 2\n3 1 5\n', 'YES\r\n'),
        edge('1\n3 3 0\n1 2 1\n2 3 1\n1 3 3\n', 'NO\r\n'),
        stress('2\n4 4 1\n1 2 3\n2 3 3\n3 4 3\n4 1 3\n4 2 10\n3 2 1\n1 2 2\n2 3 2\n3 1 1\n', 'YES\r\nNO\r\n'),
    ]
