from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n3\n', 'YES\r\n'),
        edge('2\n1 1\n', 'NO\r\n'),
        stress('5\n1 2 3 4 5\n', 'YES\r\n'),
    ]
