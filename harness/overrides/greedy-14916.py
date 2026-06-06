from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n', '-1\r\n'),
        edge('2\n', '1\r\n'),
        edge('3\n', '-1\r\n'),
        edge('4\n', '2\r\n'),
        edge('13\n', '5\r\n'),
        stress('100000\n', '20000\r\n'),
    ]
