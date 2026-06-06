from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\nR\n', '0\r\n'),
        edge('5\nRRRRR\n', '0\r\n'),
        edge('5\nRBRBR\n', '2\r\n'),
        edge('8\nBBRBRRBB\n', '3\r\n'),
        edge('10\nRRRBBBBRRR\n', '3\r\n'),
        stress('100\nRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRBRB\n', '49\r\n'),
    ]
