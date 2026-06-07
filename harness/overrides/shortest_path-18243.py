from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 1\n1 2\n', 'Small World!\r\n'),
        edge('3 1\n1 2\n', 'Big World!\r\n'),
        stress('7 6\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n', 'Small World!\r\n'),
    ]
