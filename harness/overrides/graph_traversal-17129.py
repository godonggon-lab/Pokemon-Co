from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 2\n23\n', 'TAK\r\n1\r\n'),
        edge('2 2\n21\n10\n', 'NIE\r\n'),
        edge('1 1\n2\n', 'NIE\r\n'),
        edge('2 2\n20\n03\n', 'TAK\r\n2\r\n'),
        edge('2 3\n210\n113\n', 'NIE\r\n'),
        stress('4 5\n20000\n11110\n00030\n01110\n', 'TAK\r\n7\r\n'),
    ]
