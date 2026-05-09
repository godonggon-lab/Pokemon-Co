from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("Oak\n", "Oak 100.0000\n"),
        edge("Oak\nPine\n", "Oak 50.0000\nPine 50.0000\n"),
        edge("Pine\nOak\nPine\n", "Oak 33.3333\nPine 66.6667\n"),
        edge("A\nB\nC\nA\n", "A 50.0000\nB 25.0000\nC 25.0000\n"),
        edge("Red Maple\nRed Maple\nWhite Oak\n", "Red Maple 66.6667\nWhite Oak 33.3333\n"),
        stress("C\nB\nA\nA\nB\nA\n", "A 50.0000\nB 33.3333\nC 16.6667\n"),
    ]
