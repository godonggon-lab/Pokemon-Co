from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1\n"),
        edge("1\n1 5\n"),
        edge("1\n2 4\n"),
        edge("3\n1 1\n2 3\n3 5\n"),
        edge("4\n5 10\n10 20\n13 29\n30 30\n"),
        stress("5\n1 30\n2 30\n15 30\n20 30\n29 30\n"),
    ]
