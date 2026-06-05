from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, fuzz, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\nR\n', '1 1\r\n'),
        edge('5\nRRRBB\nGGBBB\nBBBRR\nBBRRR\nRRRRR\n', '4 3\r\n'),
        stress('10\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\nRGBRGBRGBR\n', '10 7\r\n'),
    ]
