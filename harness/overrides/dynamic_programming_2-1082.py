from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n6 7 8\n21\n"),
        edge("2\n1 10\n9\n"),
        stress("5\n5 3 4 6 7\n24\n"),
    ]
