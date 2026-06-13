from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1 1\n0\n', 'YES\r\n'),
        edge('2 2\n11\n00\n', 'NO\r\n'),
        edge('2 2\n00\n00\n', 'YES\r\n'),
        edge('3 3\n010\n010\n010\n', 'YES\r\n'),
        edge('3 3\n000\n111\n000\n', 'NO\r\n'),
        stress('4 5\n01010\n01010\n00010\n11110\n', 'YES\r\n'),
    ]
