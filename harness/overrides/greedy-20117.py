from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n10\n', '10\r\n'),
        edge('5\n1 2 3 4 5\n', '12\r\n'),
        stress('8\n9 1 8 2 7 3 6 4\n', '30\r\n'),
    ]
