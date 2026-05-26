from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4 2\n1111\n1111\n"),
        edge("5 3\n11011\n00111\n"),
        stress("8 3\n11101111\n10111101\n"),
    ]
