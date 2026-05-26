from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n2 1 2\n"),
        edge("3\n1 1\n1 1\n1 1\n"),
        stress("4\n2 1 2\n2 2 3\n2 1 3\n3 1 2 3\n"),
    ]
