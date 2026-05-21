from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n1 7 14\n7\n"),
        edge("3\n1 7 14\n2\n"),
        edge("3\n10 20 30\n5\n"),
        edge("4\n5 10 15 20\n14\n"),
        stress("5\n100 200 300 400 500\n250\n"),
    ]
