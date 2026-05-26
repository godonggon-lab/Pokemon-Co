from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2 1\n1 1 1 2 5\n"),
        edge("4 4 3\n1 1 1 2 5\n2 2 2 3 7\n4 4 3 1 9\n"),
        stress("5 6 5\n1 1 2 2 4\n2 3 3 3 8\n5 6 4 1 10\n4 2 5 4 6\n3 5 1 2 7\n"),
    ]
