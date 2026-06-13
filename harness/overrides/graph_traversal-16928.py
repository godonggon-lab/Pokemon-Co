from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('0 0\n', '17\r\n'),
        edge('1 1\n2 100\n99 1\n', '1\r\n'),
        edge('1 0\n2 99\n', '2\r\n'),
        edge('1 0\n2 7\n', '17\r\n'),
        edge('0 1\n99 1\n', '17\r\n'),
        stress('3 2\n3 22\n5 8\n11 26\n27 1\n21 9\n', '14\r\n'),
    ]
