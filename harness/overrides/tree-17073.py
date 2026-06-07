from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2 10\n1 2\n', '10.0\r\n'),
        edge('3 9\n1 2\n1 3\n', '4.5\r\n'),
        stress('6 12\n1 2\n2 3\n2 4\n1 5\n5 6\n', '4.0\r\n'),
    ]
