from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1\n5 4\n", "5\n"),
        edge("4\n2 3 1\n5 2 4 1\n", "18\n"),
        edge("5\n1 1 1 1\n10 9 8 7 6\n", "34\n"),
        edge("5\n10 20 30 40\n1 100 100 100 100\n", "100\n"),
        edge("6\n3 3 4 5 6\n5 4 3 2 1 10\n", "55\n"),
        stress("7\n1 2 3 4 5 6\n10 9 8 7 6 5 4\n", "140\n"),
    ]
