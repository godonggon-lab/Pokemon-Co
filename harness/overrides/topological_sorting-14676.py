from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1 3\n1 2\n1 1\n1 2\n2 1\n', 'King-God-Emperor\r\n'),
        edge('2 1 1\n1 2\n1 2\n', 'Lier!\r\n'),
        stress('4 3 7\n1 2\n1 3\n2 4\n1 1\n1 2\n1 3\n1 4\n2 1\n2 4\n2 2\n', 'King-God-Emperor\r\n'),
    ]
