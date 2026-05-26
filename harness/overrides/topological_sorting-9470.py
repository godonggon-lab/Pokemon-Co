from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 3 2\n1 3\n2 3\n"),
        edge("1\n2 4 4\n1 3\n2 3\n3 4\n2 4\n"),
        stress("2\n3 5 5\n1 3\n2 3\n3 4\n3 5\n4 5\n4 4 3\n1 2\n1 3\n2 4\n"),
    ]
