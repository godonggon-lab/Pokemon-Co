from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n1\n', '1\r\n1\r\n'),
        edge('3\n2\n3\n1\n', '3\r\n1\r\n2\r\n3\r\n'),
        edge('2\n1\n1\n', '1\r\n1\r\n'),
        edge('4\n2\n1\n4\n3\n', '4\r\n1\r\n2\r\n3\r\n4\r\n'),
        edge('5\n2\n3\n1\n5\n4\n', '5\r\n1\r\n2\r\n3\r\n4\r\n5\r\n'),
        stress('6\n2\n1\n4\n5\n3\n6\n', '6\r\n1\r\n2\r\n3\r\n4\r\n5\r\n6\r\n'),
    ]
