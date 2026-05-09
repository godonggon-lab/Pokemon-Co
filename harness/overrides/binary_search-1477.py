from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0 1 10\n\n"),
        edge("0 2 10\n\n"),
        edge("1 1 10\n5\n"),
        edge("2 1 20\n5 15\n"),
        edge("3 2 100\n20 50 80\n"),
        stress("5 3 200\n20 60 90 140 170\n"),
    ]
