from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n7\n"),
        edge("2 1\n9 1\n"),
        edge("3 2\n4 2 9\n"),
        edge("4 2\n10 1 7 3\n"),
        edge("4 4\n4 3 2 1\n"),
        stress("8 3\n8 1 7 2 6 3 5 4\n"),
    ]
