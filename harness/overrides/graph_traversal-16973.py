from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n0 0 0\n0 0 0\n0 0 0\n1 1 1 1 3 3\n"),
        edge("4 4\n0 0 0 0\n0 1 0 0\n0 0 0 0\n0 0 0 0\n2 2 1 1 3 3\n"),
        stress("5 5\n0 0 0 0 0\n0 1 0 1 0\n0 0 0 0 0\n0 1 0 0 0\n0 0 0 0 0\n2 2 1 1 4 4\n"),
    ]
