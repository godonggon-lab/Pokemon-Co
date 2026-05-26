from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n8 5\n"),
        edge("3\n8 5\n1 100\n3 5\n"),
        stress("5\n10 3\n5 4\n8 2\n1 10\n7 3\n"),
    ]
