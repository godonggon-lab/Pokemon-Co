from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n1 1\n"),
        edge("2 1\n1 3\n"),
        edge("3 2\n1 2 3\n"),
        edge("4 3\n1 4 2 5\n"),
        edge("5 10\n1 10 1 10 1\n"),
        stress("8 20\n1 3 6 10 15 21 28 36\n"),
    ]
