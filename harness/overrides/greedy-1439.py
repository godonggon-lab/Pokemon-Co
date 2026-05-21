from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0\n"),
        edge("1\n"),
        edge("000000\n"),
        edge("010101\n"),
        edge("0001100\n"),
        stress(("01" * 50) + "\n"),
    ]
