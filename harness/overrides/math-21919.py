from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("1\n2\n"),
        edge("4\n2 3 4 5\n"),
        edge("5\n4 6 8 9 10\n"),
        edge("6\n2 2 3 3 5 5\n"),
        stress("8\n997 991 2 4 6 8 10 12\n"),
    ]
