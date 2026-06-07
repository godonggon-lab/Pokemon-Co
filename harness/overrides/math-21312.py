from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 2 3\n', '3\r\n'),
        edge('2 4 6\n', '48\r\n'),
        edge('1 1 1\n', '1\r\n'),
        edge('2 3 4\n', '3\r\n'),
        edge('9 8 7\n', '63\r\n'),
        stress('100 101 102\n', '101\r\n'),
    ]
