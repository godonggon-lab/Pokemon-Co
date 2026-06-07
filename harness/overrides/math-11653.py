from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n', ''),
        edge('2\n', '2\r\n'),
        edge('12\n', '2\r\n2\r\n3\r\n'),
        edge('999\n', '3\r\n3\r\n3\r\n37\r\n'),
        edge('9973\n', '9973\r\n'),
        stress('100000\n', '2\r\n2\r\n2\r\n2\r\n2\r\n5\r\n5\r\n5\r\n5\r\n5\r\n'),
    ]
