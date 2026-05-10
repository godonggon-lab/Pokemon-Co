from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n", "5\n"),
        edge("2\n10 20\n1 2\n", "20\n"),
        edge("3\n10 1 10\n1 2\n2 3\n", "20\n"),
        edge("4\n100 1 1 1\n1 2\n1 3\n1 4\n", "100\n"),
        edge("4\n1 10 10 10\n1 2\n1 3\n1 4\n", "30\n"),
        stress("5\n10 20 30 40 50\n1 2\n1 3\n3 4\n3 5\n", "110\n"),
    ]
