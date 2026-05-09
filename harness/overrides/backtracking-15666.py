from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n7\n"),
        edge("2 2\n1 1\n"),
        edge("3 2\n1 1 2\n"),
        edge("4 2\n9 7 9 1\n"),
        edge("5 3\n2 2 1 1 3\n"),
        stress("8 4\n4 4 3 3 2 2 1 1\n"),
    ]
