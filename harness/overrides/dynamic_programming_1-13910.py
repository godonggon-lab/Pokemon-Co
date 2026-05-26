from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 1\n2\n"),
        edge("10 3\n1 3 4\n"),
        stress("31 4\n3 5 9 11\n"),
    ]
