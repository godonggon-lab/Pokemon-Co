from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n0 2\n0 1 5\n1 2 4\n0 2 2\n"),
        edge("4 4\n0 3\n0 1 10\n1 3 3\n0 2 5\n2 3 4\n"),
        stress("5 6\n1 4\n0 1 7\n1 2 6\n2 4 5\n1 3 4\n3 4 9\n0 4 2\n"),
    ]
