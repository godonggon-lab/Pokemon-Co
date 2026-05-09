from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nB\n", "1\n"),
        edge("1\nR\n", "1\n"),
        edge("4\nBBBB\n", "1\n"),
        edge("4\nBRBR\n", "3\n"),
        edge("8\nBBRRRBBB\n", "2\n"),
        stress("10\nRBRRBBBRBR\n", "4\n"),
    ]
