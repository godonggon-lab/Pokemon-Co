from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 2 3 4 5 1 2 3 4 5\n"),
        edge("1 1 1 1 1 1 1 1 1 1\n"),
        stress("5 4 3 2 1 5 4 3 2 1\n"),
    ]
