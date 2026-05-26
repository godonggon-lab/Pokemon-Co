from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 1 0\n1 2\n2 3\n"),
        edge("5 1 1\n1 2\n2 3\n3 4\n3 5\n"),
        stress("7 3 2\n1 2\n2 3\n3 4\n3 5\n5 6\n5 7\n"),
    ]
