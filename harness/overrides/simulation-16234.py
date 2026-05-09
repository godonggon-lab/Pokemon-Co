from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 20 50\n50 30\n20 40\n"),
        edge("2 40 50\n50 30\n20 40\n"),
        edge("3 5 10\n10 15 20\n20 30 25\n40 22 10\n"),
        edge("4 10 20\n10 100 20 90\n80 100 60 70\n70 20 30 40\n50 20 100 10\n"),
        edge("5 1 100\n1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15\n16 17 18 19 20\n21 22 23 24 25\n"),
        stress("6 15 35\n10 20 30 40 50 60\n20 30 40 50 60 70\n30 40 50 60 70 80\n40 50 60 70 80 90\n50 60 70 80 90 100\n60 70 80 90 100 110\n"),
    ]
