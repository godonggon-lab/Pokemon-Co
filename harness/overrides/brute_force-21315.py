from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4\n2 1 4 3\n"),
        edge("5\n3 2 5 4 1\n"),
        edge("5\n3 2 4 1 5\n"),
        edge("8\n6 5 8 7 1 2 3 4\n"),
        edge("8\n4 3 1 2 8 7 5 6\n"),
        stress("10\n8 7 5 6 1 2 3 4 10 9\n"),
    ]
