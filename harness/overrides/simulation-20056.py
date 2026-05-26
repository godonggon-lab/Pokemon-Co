from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4 1 1\n1 1 5 1 2\n"),
        edge("4 2 2\n1 1 5 1 2\n1 3 5 1 6\n"),
        stress("5 4 3\n1 1 5 2 2\n2 2 4 3 4\n3 3 3 1 6\n5 5 2 4 0\n"),
    ]
