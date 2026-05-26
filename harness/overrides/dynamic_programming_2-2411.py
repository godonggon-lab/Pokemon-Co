from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3 1 0\n2 2\n"),
        edge("4 4 2 1\n2 2\n3 3\n2 3\n"),
        stress("5 5 3 2\n2 2\n3 4\n5 5\n2 3\n4 4\n"),
    ]
