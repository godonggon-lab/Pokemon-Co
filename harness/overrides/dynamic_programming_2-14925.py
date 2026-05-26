from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n"),
        edge("3 4\n0 0 1 0\n0 0 0 0\n1 0 0 0\n"),
        stress("6 7\n0 0 0 0 1 0 0\n0 0 0 0 1 0 0\n0 0 0 0 0 0 0\n1 0 0 0 0 1 0\n0 0 0 0 0 0 0\n0 1 0 0 0 0 0\n"),
    ]
