from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 0 3\n"),
        edge("2 1 3\n1 1\n"),
        stress("5 3 5\n1 1\n3 2\n2 4\n"),
    ]
