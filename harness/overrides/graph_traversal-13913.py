from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5 17\n', '4\r\n5 4 8 16 17\r\n'),
        edge('10 3\n', '7\r\n10 9 8 7 6 5 4 3\r\n'),
        stress('1 20\n', '5\r\n1 2 4 5 10 20\r\n'),
    ]
