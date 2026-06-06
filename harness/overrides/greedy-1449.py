from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n5\n', '1\r\n'),
        edge('4 2\n1 2 100 101\n', '2\r\n'),
        edge('4 3\n1 2 3 4\n', '2\r\n'),
        edge('5 4\n10 1 6 2 3\n', '3\r\n'),
        edge('6 1\n1 2 3 4 5 6\n', '6\r\n'),
        stress('20 5\n1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58\n', '10\r\n'),
    ]
