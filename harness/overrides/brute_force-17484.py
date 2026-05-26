from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\n1 2\n3 4\n"),
        edge("3 3\n1 9 1\n9 1 9\n1 9 1\n"),
        stress("5 4\n5 8 5 1\n3 2 7 6\n9 1 4 8\n2 6 3 5\n7 4 2 9\n"),
    ]
