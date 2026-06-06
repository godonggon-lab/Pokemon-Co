from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('10 1 10 2 1\n', '6\r\n'),
        edge('100 2 1 1 0\n', 'use the stairs\r\n'),
        edge('10 5 5 3 2\n', '0\r\n'),
        edge('10 1 10 0 1\n', 'use the stairs\r\n'),
        stress('100000 1 99999 3 2\n', '33336\r\n'),
    ]
