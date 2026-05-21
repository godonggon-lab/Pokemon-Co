from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nR\n"),
        edge("5\nRRRRR\n"),
        edge("5\nRBRBR\n"),
        edge("8\nBBRBRRBB\n"),
        edge("10\nRRRBBBBRRR\n"),
        stress("100\n" + "RBRB" * 25 + "\n"),
    ]
