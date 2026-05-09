from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("1 7\n3\n"),
        edge("3 15\n1\n5\n12\n"),
        edge("2 3\n2\n4\n"),
        edge("4 11\n1\n5\n5\n7\n"),
        stress("5 100\n1\n3\n7\n11\n50\n"),
    ]
