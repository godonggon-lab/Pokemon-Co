from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 2\n1 2\n2 3\n"),
        edge("4 4\n1 2\n2 3\n3 1\n3 4\n"),
        stress("6 5\n1 2\n2 3\n4 5\n5 6\n6 4\n"),
    ]
