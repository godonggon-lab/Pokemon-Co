from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 2\n1 2 1 2 1 2\n"),
        edge("2 3\n1 1 1 1\n"),
        stress("4 4\n3 2 1 2 3 2 1 2\n"),
    ]
