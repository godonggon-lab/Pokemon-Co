from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5\n3 2 3 3 4\n5\n2 3 4 6 8\n"),
        edge("6\n3 3 3 3 3 5\n6\n1 2 3 4 5 9\n"),
        stress("5\n2 1 2 3 3\n3\n1 2 3\n"),
    ]
