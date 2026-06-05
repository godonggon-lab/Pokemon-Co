from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n', '1\r\n'),
        edge('1 2\n', '2\r\n'),
        edge('1 21\n', '3\r\n'),
        edge('2 162\n', '5\r\n'),
        edge('4 42\n', '-1\r\n'),
        stress('100 40021\n', '5\r\n'),
    ]
