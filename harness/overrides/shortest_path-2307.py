from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n1 2 1\n2 3 1\n1 3 5\n"),
        edge("4 4\n1 2 1\n2 4 1\n1 3 1\n3 4 1\n"),
        stress("5 6\n1 2 2\n2 5 2\n1 3 3\n3 4 3\n4 5 3\n2 3 1\n"),
    ]
