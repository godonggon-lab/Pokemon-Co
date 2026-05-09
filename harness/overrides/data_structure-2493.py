from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n", "0 \n"),
        edge("2\n1 2\n", "0 0 \n"),
        edge("2\n2 1\n", "0 1 \n"),
        edge("5\n6 9 5 7 4\n", "0 0 2 2 4 \n"),
        edge("5\n5 4 3 2 1\n", "0 1 2 3 4 \n"),
        stress("8\n3 7 7 2 9 1 5 4\n", "0 0 2 3 0 5 5 7 \n"),
    ]
