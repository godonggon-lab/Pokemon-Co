from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 2\n1 1 2\n1 2 3\n1\n1\n"),
        edge("4 3\n2 1 2 3\n1 3 4\n1 2 4\n2\n1 2\n"),
        stress("5 4\n2 1 2 3\n1 3 4\n2 2 4 5\n1 1 5\n1\n1\n"),
    ]
