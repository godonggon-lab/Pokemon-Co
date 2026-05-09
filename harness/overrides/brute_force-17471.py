from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n10 20\n1 2\n1 1\n"),
        edge("3\n1 2 3\n1 2\n2 1 3\n1 2\n"),
        edge("4\n5 5 5 5\n1 2\n2 1 3\n2 2 4\n1 3\n"),
        edge("4\n1 10 100 1000\n0\n0\n0\n0\n"),
        edge("5\n10 20 30 40 50\n2 2 3\n2 1 4\n2 1 5\n1 2\n1 3\n"),
        stress("6\n2 3 5 7 11 13\n2 2 3\n2 1 4\n2 1 5\n2 2 6\n1 3\n1 4\n"),
    ]
