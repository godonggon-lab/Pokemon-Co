from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4\n1 2\n2 3\n3 4\n"),
        edge("4\n1 2\n1 3\n1 4\n"),
        stress("6\n1 2\n2 3\n2 4\n4 5\n4 6\n"),
    ]
