from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n1 2\n0 0\n"),
        edge("5 3\n0 0 1 0 0\n0 0 2 0 1\n0 1 2 0 0\n0 0 1 0 0\n0 0 0 0 2\n"),
        stress("6 2\n1 0 2 0 1 0\n0 0 0 0 0 0\n2 0 1 0 2 0\n0 0 0 1 0 0\n1 0 2 0 0 1\n0 0 0 0 2 0\n"),
    ]
