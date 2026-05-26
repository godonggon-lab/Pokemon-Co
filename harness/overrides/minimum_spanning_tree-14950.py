from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3 1\n1 2 3\n2 3 4\n1 3 10\n"),
        edge("4 5 2\n1 2 1\n2 3 2\n3 4 3\n1 4 10\n2 4 4\n"),
        stress("5 7 3\n1 2 5\n1 3 6\n2 3 1\n2 4 7\n3 5 2\n4 5 4\n1 5 10\n"),
    ]
