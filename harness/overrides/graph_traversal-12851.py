from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5 17\n', '4\r\n2\r\n'),
        edge('0 0\n', '0\r\n1\r\n'),
        edge('10 1\n', '9\r\n1\r\n'),
        edge('1 100\n', '8\r\n2\r\n'),
        stress('0 100000\n', '22\r\n8\r\n'),
    ]
