from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1 1\n"),
        edge("2\n6 10\n"),
        edge("3\n12 18 24\n"),
        edge("3\n7 11 13\n"),
        edge("2\n100 250\n"),
        stress("3\n360 720 1080\n"),
    ]
