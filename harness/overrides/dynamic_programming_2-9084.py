from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n2\n1 2\n5\n', '3\r\n'),
        edge('2\n3\n1 5 10\n100\n2\n2 3\n10\n', '121\r\n2\r\n'),
        stress('1\n5\n1 2 5 10 20\n200\n', '47696\r\n'),
    ]
