from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 3\n', '-1\r\n'),
        edge('5 3\n', '-1\r\n'),
        edge('6 3\n', '2\r\n'),
        edge('7 3\n', '3\r\n'),
        edge('100 10\n', '10\r\n'),
        stress('100000 447\n', '-1\r\n'),
    ]
