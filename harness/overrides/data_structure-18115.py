from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n", "1 \n"),
        edge("2\n1 1\n", "2 1 \n"),
        edge("2\n2 1\n", "1 2 \n"),
        edge("3\n3 3 3\n", "1 2 3 \n"),
        edge("5\n1 1 1 1 1\n", "5 4 3 2 1 \n"),
        stress("5\n1 2 3 1 1\n", "5 2 4 1 3 \n"),
    ]
