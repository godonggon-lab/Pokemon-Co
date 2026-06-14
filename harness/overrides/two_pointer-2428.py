from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('2\n9 10\n', '1\r\n'),
        edge('3\n1 10 100\n', '0\r\n'),
        edge('1\n100\n', '0\r\n'),
        edge('4\n10 10 10 10\n', '6\r\n'),
        edge('3\n89 90 100\n', '2\r\n'),
        stress('6\n90 91 100 101 110 200\n', '7\r\n'),
    ]
