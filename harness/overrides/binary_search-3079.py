from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n7\n"),
        edge("1 3\n7\n"),
        edge("2 6\n7\n10\n"),
        edge("2 1\n7\n10\n"),
        edge("3 10\n3\n8\n10\n"),
        stress("5 100\n1\n3\n7\n11\n13\n"),
    ]
