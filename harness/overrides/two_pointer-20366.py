from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('4\n1 2 3 4\n', '0\r\n'),
        edge('5\n1 5 3 8 10\n', '0\r\n'),
        stress('8\n1 3 4 7 10 13 17 20\n', '0\r\n'),
    ]
