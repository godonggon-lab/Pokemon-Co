from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 0\n10\n', '1\r\n'),
        edge('1 1\n20\n', '2\r\n'),
        edge('3 1\n10 20 30\n', '3\r\n'),
        edge('5 3\n13 20 10 25 30\n', '6\r\n'),
        edge('5 10\n11 12 13 14 15\n', '5\r\n'),
        stress('20 15\n10 20 30 40 50 60 70 80 90 10 20 30 40 50 60 70 80 90 10 20\n', '25\r\n'),
    ]
