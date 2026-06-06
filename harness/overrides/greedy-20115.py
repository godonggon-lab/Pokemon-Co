from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n10\n', '10\r\n'),
        edge('2\n10 20\n', '25.0\r\n'),
        edge('3\n2 3 6\n', '8.5\r\n'),
        edge('5\n1 1 1 1 100\n', '102.0\r\n'),
        edge('5\n100 1 1 1 1\n', '102.0\r\n'),
        stress('20\n1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58\n', '324.0\r\n'),
    ]
