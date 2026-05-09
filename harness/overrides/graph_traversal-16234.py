from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 10\n10\n", "0\n"),
        edge("2 20 50\n50 30\n20 40\n", "1\n"),
        edge("2 1 1\n10 20\n30 40\n", "0\n"),
        edge("3 5 10\n10 15 20\n20 30 25\n40 22 10\n", "2\n"),
        edge("3 10 20\n10 30 50\n20 40 60\n30 50 70\n", "1\n"),
        stress("4 10 30\n10 100 20 90\n80 30 70 40\n50 60 55 65\n20 25 30 35\n", "4\n"),
    ]
