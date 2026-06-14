from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('3 1 1\n0900 0930\n', '690\r\n'),
        edge('5 2 3\n0900 1000\n1000 1100\n', '720\r\n'),
        edge('1 1 1\n0900 2100\n', '0\r\n'),
        edge('2 1 2\n0900 2100\n', '720\r\n'),
        edge('3 2 2\n0900 1000\n1000 1100\n', '720\r\n'),
        stress('7 4 4\n0900 0930\n0910 1000\n1100 1200\n1230 1300\n', '720\r\n'),
    ]
