from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n1\n', '1\r\n'),
        edge('3 14\n1\n5\n10\n', '5\r\n'),
        edge('4 0\n1\n5\n10\n50\n', '0\r\n'),
        edge('5 4790\n1\n10\n100\n1000\n5000\n', '20\r\n'),
        edge('6 999\n1\n3\n9\n27\n81\n243\n', '5\r\n'),
        stress('10 42000\n1\n5\n10\n50\n100\n500\n1000\n5000\n10000\n50000\n', '6\r\n'),
    ]
